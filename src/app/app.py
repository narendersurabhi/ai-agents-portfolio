from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import List

import streamlit as st

from src.agents.retrieval_agent import RetrievalAgent

DOCS_DIR = Path(os.getenv("STREAMLIT_DOCS_DIR", "data/docs"))
INDEX_DIR = Path(os.getenv("STREAMLIT_INDEX_DIR", "data/vector_index"))
BACKEND = os.getenv("VECTOR_BACKEND", "faiss")


def _ensure_directories() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)


def _run_build_pipeline() -> None:
    cmd = [
        "python",
        "-m",
        "src.pipelines.build_index",
        "--src",
        str(DOCS_DIR),
        "--out",
        str(INDEX_DIR),
        "--backend",
        BACKEND,
    ]
    subprocess.run(cmd, check=True)


def _save_uploaded_files(uploaded_files) -> List[Path]:
    saved_paths: List[Path] = []
    for uploaded in uploaded_files:
        destination = DOCS_DIR / uploaded.name
        with destination.open("wb") as fh:
            fh.write(uploaded.getbuffer())
        saved_paths.append(destination)
    return saved_paths


def _get_agent() -> RetrievalAgent:
    if "retrieval_agent" not in st.session_state:
        st.session_state.retrieval_agent = RetrievalAgent()
    return st.session_state.retrieval_agent


_ensure_directories()
st.set_page_config(page_title="Faiss RAG Workbench", layout="wide")
st.title("Faiss-backed Retrieval Playground")

st.sidebar.header("Document Ingestion")
uploaded = st.sidebar.file_uploader(
    "Upload documents to embed", accept_multiple_files=True, type=["pdf", "md", "txt"]
)

ingest_status = st.sidebar.empty()

if uploaded and st.sidebar.button("Ingest & Rebuild Index"):
    try:
        saved = _save_uploaded_files(uploaded)
        ingest_status.info(f"Saved {len(saved)} documents. Rebuilding index...")
        with st.spinner("Embedding documents and updating Faiss index..."):
            _run_build_pipeline()
            agent = _get_agent()
            if hasattr(agent.vs, "reload"):
                agent.vs.reload()
        ingest_status.success("Index rebuilt and hot-swapped.")
    except subprocess.CalledProcessError as exc:
        ingest_status.error(f"Rebuild failed: {exc}")
    except Exception as exc:  # pragma: no cover - UI feedback
        ingest_status.error(f"Unexpected error: {exc}")

st.header("Ask the Knowledge Base")
query = st.text_input("Enter your question")
run_query = st.button("Run Retrieval")

if run_query and query.strip():
    agent = _get_agent()
    with st.spinner("Running RAG retrieval..."):
        result = agent.run(query)
    st.subheader("Answer")
    st.write(result.get("answer") or "No answer produced.")

    sources = result.get("sources") or []
    if sources:
        st.subheader("Sources")
        for src in sources:
            st.write(f"- {src}")

    hits = result.get("hits") or []
    if hits:
        with st.expander("Retrieved Chunks", expanded=False):
            for hit in hits:
                chunk_id = hit.get("chunk")
                score = hit.get("score")
                score_text = f"{score:.3f}" if isinstance(score, (int, float)) else "n/a"
                st.markdown(
                    f"**{hit.get('id')}** (chunk {chunk_id}, score={score_text})"
                )
                if hit.get("text"):
                    st.write(hit["text"])
else:
    st.info("Upload new documents via the sidebar or ask a question above to test retrieval.")
