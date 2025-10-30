from __future__ import annotations

import json
from typing import Any, Dict

from fastapi import APIRouter, Body, Depends, HTTPException
import jsonschema

from agents.base import SchemaValidationError
from agents.tools import feature_stats, provider_history, rules_eval
from app.deps import get_agent_registry, get_openai_client

router = APIRouter()


def _load_schema() -> Dict[str, Any]:
    with open("schemas/claim.json", "r", encoding="utf-8") as handle:
        return json.load(handle)


CLAIM_SCHEMA = _load_schema()


@router.post("/score")
def score(  # type: ignore[override]
    claim: Dict[str, Any] = Body(..., embed=False),
    registry=Depends(get_agent_registry),
    client=Depends(get_openai_client),
) -> Dict[str, Any]:
    try:
        jsonschema.validate(claim, CLAIM_SCHEMA)
    except jsonschema.ValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": exc.message}) from exc

    triage_agent = registry.get("triage")
    provider_npi = claim["provider"]["npi"]
    payload = {
        "claim": claim,
        "rules_eval": rules_eval(claim),
        "feature_stats": feature_stats(claim["id"]),
        "provider_history": provider_history(provider_npi),
    }

    try:
        result = triage_agent.run(client, payload)
    except SchemaValidationError as exc:
        raise HTTPException(status_code=400, detail={"schema_error": str(exc)}) from exc
    return result


__all__ = ["router"]
