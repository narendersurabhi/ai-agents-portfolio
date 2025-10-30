from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from . import GuardDecision


class RelevanceGuard:
    """Checks payloads for expected structural elements."""

    name = "relevance"

    def run(
        self,
        payload: Mapping[str, Any],
        *,
        context: Mapping[str, Any] | None = None,
    ) -> GuardDecision:
        ctx = context or {}
        flow = ctx.get("flow")
        if flow == "score":
            required = {"id", "member", "provider", "lines"}
            missing = sorted(required.difference(payload.keys()))
            if missing:
                return GuardDecision(
                    handoff=True,
                    reason=f"Missing required claim keys: {', '.join(missing)}",
                )
        if flow == "explain":
            claim_id = payload.get("claim_id")
            if not isinstance(claim_id, str) or not claim_id.strip():
                return GuardDecision(
                    handoff=True,
                    reason="Explain requests must include a claim_id",
                )
        return GuardDecision(payload=deepcopy(payload))


__all__ = ["RelevanceGuard"]
