from __future__ import annotations

import os
import subprocess
import sys
from functools import lru_cache
from pathlib import Path
from typing import List, Sequence

from fastapi import UploadFile

from src.agents.retrieval_agent import RetrievalAgent


DOCS_DIR = Path(
    os.getenv("VECTOR_DOCS_DIR")
    or "data/docs"
)
INDEX_DIR = Path(
    os.getenv("VECTOR_INDEX_DIR")
    or "data/vector_index"
)
VECTOR_BACKEND = os.getenv("VECTOR_BACKEND", "faiss")


def _ensure_directories() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)


@lru_cache(maxsize=1)
def get_retrieval_agent() -> RetrievalAgent:
    _ensure_directories()
    return RetrievalAgent()


async def save_documents(files: Sequence[UploadFile]) -> List[str]:
    _ensure_directories()
    saved: List[str] = []
    for file in files:
        try:
            if not file.filename:
                continue
            name = Path(file.filename).name
            dest = DOCS_DIR / name
            content = await file.read()
            with dest.open("wb") as fh:
                fh.write(content)
            saved.append(name)
        finally:
            await file.close()
    return saved


def rebuild_index() -> None:
    _ensure_directories()
    cmd = [
        sys.executable,
        "-m",
        "src.pipelines.build_index",
        "--src",
        str(DOCS_DIR),
        "--out",
        str(INDEX_DIR),
        "--backend",
        VECTOR_BACKEND,
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    agent = get_retrieval_agent()
    reload_fn = getattr(agent.vs, "reload", None)
    if callable(reload_fn):
        reload_fn()


def run_retrieval(question: str, top_k: int | None = None, model: str | None = None) -> dict:
    agent = get_retrieval_agent()
    original_top_k = agent.top_k
    original_model = getattr(agent, "model", None)
    try:
        if top_k is not None:
            agent.top_k = max(1, int(top_k))
        if model:
            agent.model = model
        return agent.run(question)
    finally:
        agent.top_k = original_top_k
        if original_model is not None:
            agent.model = original_model
