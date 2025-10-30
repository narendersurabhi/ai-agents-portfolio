from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from agents.registry import AgentRegistry
from agents.tools import (
    feature_stats,
    provider_history,
    render_pdf,
    rules_eval,
)


@dataclass
class ManagerConfig:
    hitl_threshold: float = 0.85


class ManagerAgent:
    """Coordinates multi-agent workflows for the API routes."""

    def __init__(
        self,
        registry: AgentRegistry,
        client: Any,
        config: ManagerConfig | None = None,
    ) -> None:
        self._registry = registry
        self._client = client
        self._config = config or ManagerConfig()

    @property
    def hitl_threshold(self) -> float:
        return self._config.hitl_threshold

    def run(self, flow: str, **kwargs: Any) -> Mapping[str, Any]:
        if flow == "score":
            claim = kwargs["claim"]
            return self._run_score(claim)
        if flow == "explain":
            claim_id = kwargs["claim_id"]
            notes = kwargs.get("notes")
            return self._run_explain(claim_id, notes)
        raise ValueError(f"Unsupported manager flow: {flow}")

    def _run_score(self, claim: Mapping[str, Any]) -> Mapping[str, Any]:
        agent = self._registry.get("triage")
        payload = {
            "claim": claim,
            "rules_eval": rules_eval(claim),
            "feature_stats": feature_stats(claim.get("id", "")),
            "provider_history": provider_history(claim.get("provider", {}).get("npi", "")),
        }
        return agent.run(self._client, payload)

    def _run_explain(self, claim_id: str, notes: str | None) -> Mapping[str, Any]:
        investigator = self._registry.get("investigator")
        investigation = investigator.run(
            self._client,
            {"claim_id": claim_id, "notes": notes},
        )
        explainer = self._registry.get("explainer")
        explanation = explainer.run(
            self._client,
            {"claim_id": claim_id, "investigation": investigation},
        )
        pdf = render_pdf({"claim_id": claim_id, "summary": explanation.get("summary", "")})
        explanation["report_url"] = pdf["report_url"]
        explainer.enforce_schema(explanation)
        return {"investigation": investigation, "explanation": explanation}


__all__ = ["ManagerAgent", "ManagerConfig"]
