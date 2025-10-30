from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from agents.base import SchemaValidationError
from agents.tools import render_pdf
from app.deps import get_agent_registry, get_openai_client

router = APIRouter()


class ExplainRequest(BaseModel):
    claim_id: str = Field(..., min_length=1)
    notes: str | None = None


@router.post("/explain")
def explain(
    request: ExplainRequest,
    registry=Depends(get_agent_registry),
    client=Depends(get_openai_client),
) -> Dict[str, Any]:
    investigator = registry.get("investigator")
    try:
        investigation = investigator.run(
            client,
            {
                "claim_id": request.claim_id,
                "notes": request.notes,
            },
        )
    except SchemaValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": str(exc)}) from exc

    explainer = registry.get("explainer")
    try:
        explanation = explainer.run(
            client,
            {
                "claim_id": request.claim_id,
                "investigation": investigation,
            },
        )
    except SchemaValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": str(exc)}) from exc

    pdf = render_pdf({"claim_id": request.claim_id, "summary": explanation["summary"]})
    explanation["report_url"] = pdf["report_url"]
    explainer.enforce_schema(explanation)
    return explanation


__all__ = ["router", "ExplainRequest"]
