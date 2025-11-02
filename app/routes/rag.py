from __future__ import annotations

import subprocess
from typing import List

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.services.rag import rebuild_index, run_retrieval, save_documents

router = APIRouter(prefix="/api/rag", tags=["retrieval"])


class QueryRequest(BaseModel):
    question: str = Field(..., description="User question to run through retrieval pipeline.")
    top_k: int | None = Field(
        default=None,
        ge=1,
        le=20,
        description="Optional override for number of chunks used to synthesize answer.",
    )
    model: str | None = Field(
        default=None,
        description="Optional override for LLM model identifier.",
    )


class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
    hits: List[dict]


@router.post("/documents")
async def upload_documents(files: List[UploadFile] = File(...)) -> dict:
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded.")
    saved = await save_documents(files)
    if not saved:
        raise HTTPException(status_code=400, detail="No valid files uploaded.")
    return {"saved": len(saved), "files": saved}


@router.post("/reindex")
def rebuild_vector_index() -> dict:
    try:
        rebuild_index()
    except subprocess.CalledProcessError as exc:  # pragma: no cover - operational path
        raise HTTPException(status_code=500, detail=f"Index rebuild failed: {exc}") from exc
    return {"status": "ok"}


@router.post("/query", response_model=QueryResponse)
def run_query(payload: QueryRequest) -> QueryResponse:
    question = payload.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question must not be empty.")
    result = run_retrieval(question, top_k=payload.top_k, model=payload.model)
    return QueryResponse(
        answer=result.get("answer") or "",
        sources=result.get("sources") or [],
        hits=result.get("hits") or [],
    )
