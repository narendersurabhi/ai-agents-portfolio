from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from agents.base import SchemaValidationError
from agents.manager import ManagerAgent
from agents.guards import GuardChain
from app.deps import (
    HandoffPublisher,
    get_guard_chain,
    get_handoff_publisher,
    get_manager_agent,
)

router = APIRouter()


class ExplainRequest(BaseModel):
    claim_id: str = Field(..., min_length=1)
    notes: str | None = None


@router.post("/explain")
def explain(
    request: ExplainRequest,
    guard_chain: GuardChain = Depends(get_guard_chain),
    manager: ManagerAgent = Depends(get_manager_agent),
    publisher: HandoffPublisher = Depends(get_handoff_publisher),
) -> Dict[str, Any]:
    guard_payload = request.model_dump()
    guard_outcome = guard_chain.run(guard_payload, context={"flow": "explain"})
    if guard_outcome.handoff:
        publisher.publish(
            {
                "flow": "explain",
                "claim_id": guard_payload.get("claim_id"),
                "guard": guard_outcome.guard,
                "reason": guard_outcome.reason,
            }
        )
        return {
            "handoff": True,
            "guard": guard_outcome.guard,
            "reason": guard_outcome.reason,
        }

    sanitized = dict(guard_outcome.payload)
    try:
        manager_payload = manager.run(
            "explain",
            claim_id=sanitized.get("claim_id"),
            notes=sanitized.get("notes"),
        )
    except SchemaValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": str(exc)}) from exc

    explanation = manager_payload.get("explanation", {})
    investigation = manager_payload.get("investigation")
    envelope: Dict[str, Any] = {
        "handoff": False,
        "result": explanation,
        "investigation": investigation,
    }
    recommendation = explanation.get("recommendation") if isinstance(explanation, dict) else None
    if recommendation in {"manual_review", "deny"}:
        reason = f"Recommendation '{recommendation}' requires human review"
        envelope.update({"handoff": True, "reason": reason})
        publisher.publish(
            {
                "flow": "explain",
                "claim_id": explanation.get("claim_id") if isinstance(explanation, dict) else None,
                "reason": reason,
                "recommendation": recommendation,
            }
        )
    return envelope


__all__ = ["router", "ExplainRequest"]
