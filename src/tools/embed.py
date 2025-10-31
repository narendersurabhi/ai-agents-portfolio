from __future__ import annotations

from typing import Iterable, List

import os
from openai import OpenAI
from openai import OpenAIError


_EMBED_MODEL_DEFAULT = os.getenv("EMBED_MODEL", "text-embedding-3-small")


def _client() -> OpenAI:
    return OpenAI()


def _fallback_embed_texts(texts: Iterable[str], dim: int = 256) -> List[List[float]]:
    # Very small, deterministic hashing-based embedding to avoid external deps
    import hashlib
    import math
    out: List[List[float]] = []
    for t in texts:
        vec = [0.0] * dim
        for tok in t.split():
            h = hashlib.md5(tok.lower().encode("utf-8")).digest()
            # take two bytes as index
            idx = (h[0] << 8 | h[1]) % dim
            vec[idx] += 1.0
        # L2 normalize
        norm = math.sqrt(sum(x * x for x in vec)) or 1.0
        out.append([x / norm for x in vec])
    return out


def embed_texts(texts: Iterable[str], model: str | None = None) -> List[List[float]]:
    model = model or _EMBED_MODEL_DEFAULT
    texts_list = list(texts)
    if not texts_list:
        return []
    try:
        client = _client()
        resp = client.embeddings.create(input=texts_list, model=model)
        return [d.embedding for d in resp.data]
    except OpenAIError:
        # Missing or invalid API key, fall back to local hashed embeddings
        return _fallback_embed_texts(texts_list)
    except Exception:
        return _fallback_embed_texts(texts_list)


def embed_text(text: str, model: str | None = None) -> List[float]:
    out = embed_texts([text], model=model)
    return out[0] if out else []


def cosine_similarity(a: List[float], b: List[float]) -> float:
    if not a or not b:
        return 0.0
    # Avoid import of numpy for portability
    import math

    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)
