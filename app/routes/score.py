from __future__ import annotations

import json
from typing import Any, Dict

from fastapi import APIRouter, Body, Depends, HTTPException
import jsonschema

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


def _load_schema() -> Dict[str, Any]:
    with open("schemas/claim.json", "r", encoding="utf-8") as handle:
        return json.load(handle)


CLAIM_SCHEMA = _load_schema()


@router.post("/score")
def score(  # type: ignore[override]
    claim: Dict[str, Any] = Body(..., embed=False),
    guard_chain: GuardChain = Depends(get_guard_chain),
    manager: ManagerAgent = Depends(get_manager_agent),
    publisher: HandoffPublisher = Depends(get_handoff_publisher),
) -> Dict[str, Any]:
    try:
        jsonschema.validate(claim, CLAIM_SCHEMA)
    except jsonschema.ValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": exc.message}) from exc

    guard_outcome = guard_chain.run(claim, context={"flow": "score"})
    if guard_outcome.handoff:
        handoff_payload = {
            "flow": "score",
            "claim_id": claim.get("id"),
            "guard": guard_outcome.guard,
            "reason": guard_outcome.reason,
        }
        publisher.publish(handoff_payload)
        return {
            "handoff": True,
            "guard": guard_outcome.guard,
            "reason": guard_outcome.reason,
        }
    sanitized_claim = guard_outcome.payload
    try:
        result = manager.run("score", claim=sanitized_claim)
    except SchemaValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": str(exc)}) from exc
    envelope: Dict[str, Any] = {"handoff": False, "result": result}
    handoff_reasons: list[str] = []
    risk_score = float(result.get("risk_score", 0.0)) if isinstance(result, dict) else 0.0
    if risk_score >= manager.hitl_threshold:
        handoff_reasons.append(
            f"Risk score {risk_score:.2f} exceeds HITL threshold {manager.hitl_threshold:.2f}"
        )
    action = result.get("action") if isinstance(result, dict) else None
    if action in {"manual_review", "deny"}:
        handoff_reasons.append(f"Action '{action}' requires human review")
    if handoff_reasons:
        reason = "; ".join(handoff_reasons)
        envelope.update({"handoff": True, "reason": reason})
        publisher.publish(
            {
                "flow": "score",
                "claim_id": result.get("claim_id") if isinstance(result, dict) else None,
                "reason": reason,
                "risk_score": risk_score,
                "action": action,
            }
        )
    return envelope


__all__ = ["router"]
