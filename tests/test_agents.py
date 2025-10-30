from __future__ import annotations

import json
from typing import Any, List

import pytest
from fastapi.testclient import TestClient

from agents.manager import ManagerAgent, ManagerConfig
from app import deps
from app.main import app


class StubOpenAI:
    def __init__(self, outputs: List[dict[str, Any]]) -> None:
        self._outputs = outputs
        self.calls: List[dict[str, Any]] = []

    class _Responses:
        def __init__(self, outer: "StubOpenAI") -> None:
            self.outer = outer

        def create(self, **kwargs: Any) -> dict[str, Any]:
            self.outer.calls.append(kwargs)
            if not self.outer._outputs:
                raise RuntimeError("No stub responses remaining")
            return self.outer._outputs.pop(0)

    @property
    def responses(self) -> "StubOpenAI._Responses":
        return StubOpenAI._Responses(self)


@pytest.fixture(autouse=True)
def clear_openai_cache() -> None:
    deps.get_openai_client.cache_clear()
    deps.get_manager_agent.cache_clear()
    deps.get_guard_chain.cache_clear()
    deps.get_handoff_publisher.cache_clear()
    yield
    app.dependency_overrides.clear()
    deps.get_openai_client.cache_clear()
    deps.get_manager_agent.cache_clear()
    deps.get_guard_chain.cache_clear()
    deps.get_handoff_publisher.cache_clear()


def make_claim() -> dict[str, Any]:
    return {
        "id": "CLM-1",
        "member": {"id": "M-1", "dob": "1980-01-01", "plan_id": "P-1"},
        "provider": {"npi": "1234567890", "name": "Clinic"},
        "dos": "2024-01-01",
        "place": "office",
        "amount": 100.0,
        "lines": [
            {"cpt": "99213", "units": 2, "charge": 200.0, "dx": ["Z00.00"]}
        ],
    }


def test_score_endpoint_success() -> None:
    stub = StubOpenAI([
        {"text": json.dumps({
            "claim_id": "CLM-1",
            "risk_score": 0.42,
            "signals": ["High units"],
            "action": "manual_review",
        })}
    ])
    app.dependency_overrides[deps.get_openai_client] = lambda: stub
    app.dependency_overrides[deps.get_manager_agent] = lambda: ManagerAgent(
        deps.get_agent_registry(),
        stub,
        ManagerConfig(hitl_threshold=deps.get_settings()["hitl_threshold"]),
    )

    client = TestClient(app)
    response = client.post("/score", json=make_claim())
    assert response.status_code == 200
    data = response.json()
    assert data["handoff"] is True
    assert data["result"]["risk_score"] == pytest.approx(0.42)
    assert data["result"]["action"] == "manual_review"


def test_score_endpoint_schema_error() -> None:
    stub = StubOpenAI([
        {"text": json.dumps({"claim_id": "CLM-1", "risk_score": 0.1, "signals": [], "action": "approve"})}
    ])
    app.dependency_overrides[deps.get_openai_client] = lambda: stub
    app.dependency_overrides[deps.get_manager_agent] = lambda: ManagerAgent(
        deps.get_agent_registry(),
        stub,
        ManagerConfig(hitl_threshold=deps.get_settings()["hitl_threshold"]),
    )

    client = TestClient(app)
    bad_claim = make_claim()
    bad_claim["lines"][0].pop("cpt")
    response = client.post("/score", json=bad_claim)
    assert response.status_code == 400
    assert "schema_error" in response.json()["detail"]


def test_explain_endpoint_success() -> None:
    stub = StubOpenAI([
        {"text": json.dumps({
            "claim_id": "CLM-1",
            "suspicions": ["Upcoding"],
            "evidence": [{"source": "rules_eval", "snippet": "Units high"}],
            "peer_stats": {"units": 2.5},
        })},
        {"text": json.dumps({
            "claim_id": "CLM-1",
            "summary": "This explanation text is intentionally long enough to satisfy the schema requirements.",
            "recommendation": "manual_review",
            "citations": ["policy://billing"],
        })},
    ])
    app.dependency_overrides[deps.get_openai_client] = lambda: stub
    app.dependency_overrides[deps.get_manager_agent] = lambda: ManagerAgent(
        deps.get_agent_registry(),
        stub,
        ManagerConfig(hitl_threshold=deps.get_settings()["hitl_threshold"]),
    )

    client = TestClient(app)
    response = client.post("/explain", json={"claim_id": "CLM-1"})
    assert response.status_code == 200
    data = response.json()
    assert data["handoff"] is True
    assert data["result"]["recommendation"] == "manual_review"
    assert data["result"]["report_url"].startswith("s3://")
    assert data["investigation"]["claim_id"] == "CLM-1"
