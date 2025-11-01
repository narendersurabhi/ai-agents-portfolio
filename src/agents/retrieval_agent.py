from __future__ import annotations

from typing import Any, Dict, List, Tuple
import json
import re
import os
import sys

from openai import OpenAI
from src.tools.vector_store import LocalVectorStore
from src.tools.embed import cosine_similarity, embed_text


def _response_to_dict(payload: Any) -> Dict[str, Any]:
    if payload is None:
        return {}
    if isinstance(payload, dict):
        return payload
    for attr in ("model_dump", "to_dict", "dict"):
        fn = getattr(payload, attr, None)
        if callable(fn):
            try:
                data = fn()
            except Exception:  # pragma: no cover - defensive
                continue
            if isinstance(data, dict):
                return data
    if hasattr(payload, "__dict__") and isinstance(payload.__dict__, dict):
        return dict(payload.__dict__)
    return {}


def _extract_text_from_payload(payload: Dict[str, Any]) -> str:
    if not payload:
        return ""

    def _coerce_text(value: Any) -> str:
        if isinstance(value, dict):
            val = value.get("value") or value.get("text")
            if isinstance(val, (str, int, float)):
                return str(val)
            return ""
        if isinstance(value, (str, int, float)):
            return str(value)
        return ""

    outputs = payload.get("outputs")
    if isinstance(outputs, list) and outputs:
        text = _coerce_text(outputs[0].get("text"))
        if text:
            return text

    text = _coerce_text(payload.get("outputText"))
    if text:
        return text

    out_list = payload.get("output")
    if isinstance(out_list, list):
        chunks: List[str] = []
        for item in out_list:
            content = item.get("content") if isinstance(item, dict) else None
            if isinstance(content, list):
                for chunk in content:
                    if isinstance(chunk, dict) and chunk.get("type") in {"output_text", "text", "summary_text"}:
                        txt = _coerce_text(chunk.get("text"))
                        if txt:
                            chunks.append(txt)
        if chunks:
            return "".join(chunks)

    choices = payload.get("choices")
    if isinstance(choices, list) and choices:
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        if isinstance(message, dict):
            content = message.get("content")
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                parts = [seg.get("text") for seg in content if isinstance(seg, dict) and seg.get("text")]
                if parts:
                    return "".join(str(p) for p in parts)

    content = payload.get("content")
    if isinstance(content, str):
        return content

    return ""


def _extract_structured_json(payload: Dict[str, Any]) -> Dict[str, Any] | None:
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        return None
    message = choices[0].get("message") if isinstance(choices[0], dict) else None
    if not isinstance(message, dict):
        return None
    content = message.get("content")
    if not isinstance(content, str):
        return None

    cleaned = re.sub(r"<reasoning>.*?</reasoning>\s*", "", content, flags=re.S)
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", cleaned.strip(), flags=re.MULTILINE)

    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        return json.loads(cleaned[start : end + 1])
    except json.JSONDecodeError:
        return None

class RetrievalAgent:
    def __init__(self, top_k: int = 4, model: str | None = None):
        self.vs = LocalVectorStore("data/vector_index")
        self.top_k = top_k
        # Allow override via env for compatibility
        self.model = model or os.getenv("CHAT_MODEL") or "gpt-4o-mini"

    def _llm_answer(self, question: str, docs: List[Dict[str, Any]]) -> str:        
        context_blocks = []
        for idx, d in enumerate(docs, start=1):
            src = d.get("id", "")
            chunk = d.get("chunk", 0)
            text = d.get("text", "")[:2000]
            context_blocks.append(f"[Source {idx}] {src}#chunk{chunk}\n{text}")
        context = "\n\n".join(context_blocks)
        system = (
            "You are a concise analyst. Use only the provided context to answer."
            " Provide a short summary and a bullet list of key risks."
            " Cite sources as [Source N]. If insufficient context, say so."
        )
        user = f"Question: {question}\n\nContext:\n{context}"
        try:
            if os.getenv("LLM_DEBUG"):
                key = os.getenv("OPENAI_API_KEY") or ""
                fp = (key[:7] + "..." + key[-4:]) if key else "<missing>"
                print(f"LLM model: {self.model}; key: {fp}", file=sys.stderr)
            client = OpenAI()

            # Attempt Responses API first for modern models
            try:
                is_v5 = str(self.model).startswith("gpt-5")
                inputs = (
                    f"System:\n{system}\n\nUser:\n{user}"
                    if is_v5
                    else [
                        {"role": "system", "content": [{"type": "input_text", "text": system}]},
                        {"role": "user", "content": [{"type": "input_text", "text": user}]},
                    ]
                )
                # Prefer streaming for gpt-5 to robustly extract text deltas
                if is_v5:
                    try:
                        parts: List[str] = []
                        with client.responses.stream(
                            model=self.model, input=inputs, max_output_tokens=400
                        ) as stream:
                            for event in stream:
                                t = getattr(event, "type", None)
                                if isinstance(event, dict):
                                    t = event.get("type", t)
                                if t == "response.output_text.delta":
                                    delta = getattr(event, "delta", None)
                                    if isinstance(event, dict):
                                        delta = event.get("delta", delta)
                                    if delta:
                                        parts.append(str(delta))
                                elif t in {"response.completed", "response.completed_successfully"}:
                                    break
                        if parts:
                            return "".join(parts)
                    except Exception as e_stream:
                        if os.getenv("LLM_DEBUG"):
                            print(
                                f"Responses stream failed: {type(e_stream).__name__}: {e_stream}",
                                file=sys.stderr,
                            )
                # Fallback to non-stream create
                resp = client.responses.create(
                    model=self.model,
                    input=inputs,
                    max_output_tokens=1200 if is_v5 else 400,
                )
                payload = _response_to_dict(resp)
                text = getattr(resp, "output_text", None)
                if not text:
                    text = _extract_text_from_payload(payload)
                if not text:
                    structured = _extract_structured_json(payload)
                    if structured is not None:
                        text = json.dumps(structured)
                if text:
                    return str(text)
                if is_v5:
                    if os.getenv("LLM_DEBUG"):
                        try:
                            preview = json.dumps(payload, indent=2)[:2000]
                        except Exception:
                            preview = repr(payload)
                        print(f"Responses payload (truncated): {preview}", file=sys.stderr)
                    raise RuntimeError("responses_api_empty")
                if os.getenv("LLM_DEBUG"):
                    print("Responses API returned no text; falling back to chat", file=sys.stderr)
            except Exception as e0:
                if os.getenv("LLM_DEBUG"):
                    print(f"Responses API failed: {type(e0).__name__}: {e0}", file=sys.stderr)
                if is_v5:
                    raise

            # Chat Completions fallback with parameter negotiation
            base = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            }
            # Try legacy first
            try:
                resp = client.chat.completions.create(**{**base, "max_tokens": 400, "temperature": 0.2})
                return resp.choices[0].message.content or ""
            except Exception as e1:
                if os.getenv("LLM_DEBUG"):
                    print(f"Chat legacy failed: {type(e1).__name__}: {e1}", file=sys.stderr)
                resp = client.chat.completions.create(**{**base, "max_completion_tokens": 400})
                return resp.choices[0].message.content or ""
        except Exception as e:
            if os.getenv("LLM_DEBUG"):
                print(f"LLM call failed: {type(e).__name__}: {e}", file=sys.stderr)
            # Fallback to local summary using retrieved text (no API key/network)
            texts = [d.get("text", "") for d in docs if d.get("text")]
            sents: List[str] = []
            for t in texts:
                for s in re.split(r"(?<=[.!?])\s+", t):
                    s = s.strip()
                    if 40 <= len(s) <= 300:
                        sents.append(s)
                        if len(sents) >= 5:
                            break
                if len(sents) >= 5:
                    break
            summary = " ".join(sents[:3]) or "Context available but LLM unavailable to synthesize."

            # Heuristic risks from common terms
            risk_terms = ["hallucination", "uncertainty", "misinterpret", "outdated", "loop", "error"]
            risks: List[str] = []
            for t in texts:
                low = t.lower()
                if any(k in low for k in risk_terms):
                    risks = [
                        "Hallucination or misinterpretation under uncertainty",
                        "Over-reliance on external retrieval quality",
                        "Action/observation loops leading to errors",
                    ]
                    break
            if not risks:
                risks = [
                    "Ambiguous context may reduce answer quality",
                    "Limited grounding without full model synthesis",
                    "Potential omission of key details",
                ]

            seen = set()
            srcs: List[str] = []
            for d in docs:
                sid = str(d.get("id")) if d.get("id") is not None else ""
                if sid and sid not in seen:
                    seen.add(sid)
                    srcs.append(sid)

            lines = [
                summary,
                "",
                "### Key Risks:",
                *[f"- {r}" for r in risks],
            ]
            if srcs:
                lines.append("")
                lines.append("Sources:")
                lines.extend([f"- [#{i+1}] {s}" for i, s in enumerate(srcs)])
            return "\n".join(lines)

    def _mmr(self, q_vec: List[float], cands: List[Dict[str, Any]], k: int, lam: float = 0.75) -> List[Dict[str, Any]]:
        """
        Maximal Marginal Relevance selection from candidates based on query vector. 
        Select k items from cands balancing relevance to q_vec and diversity among selected.
        """

        if not cands:
            return []
        # Ensure embeddings are present
        pool = [c for c in cands if c.get("embedding")]
        if not pool:
            return cands[:k]
        selected: List[Dict[str, Any]] = []
        remaining = pool[:]
        # Seed with highest query similarity
        remaining.sort(key=lambda d: cosine_similarity(q_vec, d.get("embedding", [])), reverse=True)
        selected.append(remaining.pop(0))
        while remaining and len(selected) < k:
            best_idx = 0
            best_score = float("-inf")
            for i, item in enumerate(remaining):
                sim_q = cosine_similarity(q_vec, item.get("embedding", []))
                sim_sel = max(
                    cosine_similarity(item.get("embedding", []), s.get("embedding", [])) for s in selected
                )
                score = lam * sim_q - (1 - lam) * sim_sel
                if score > best_score:
                    best_score = score
                    best_idx = i
            selected.append(remaining.pop(best_idx))
        return selected[:k]

    def run(self, question: str) -> Dict[str, Any]:
        # Fetch a larger candidate pool with embeddings and text for LLM context
        pool_size = max(self.top_k * 6, self.top_k)
        cands = self.vs.search(
            question, top_k=pool_size, include_text=True, include_embedding=True
        )
        q_vec = embed_text(question)
        docs = self._mmr(q_vec, cands, self.top_k)
        answer_text = self._llm_answer(question, docs)
        # Prepare output: hide text/embedding in hits, dedup sources
        hits: List[Dict[str, Any]] = [
            {"id": d.get("id"), "score": d.get("score"), "chunk": d.get("chunk")}
            for d in docs
        ]
        seen = set()
        sources: List[str] = []
        for h in hits:
            sid = str(h["id"]) if h.get("id") is not None else ""
            if sid and sid not in seen:
                seen.add(sid)
                sources.append(sid)

        result: Dict[str, Any] = {
            "answer": answer_text,
            "sources": sources,
            "hits": hits,
        }
        return result
