from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, List

import yaml
from fastapi.testclient import TestClient

from agents.manager import ManagerAgent, ManagerConfig
from agents.tools import rules_eval
from app import deps
from app.main import app


class EvalStubOpenAI:
    class _Responses:
        def __init__(self, outer: "EvalStubOpenAI") -> None:
            self.outer = outer

        def create(self, **kwargs: Any) -> dict[str, Any]:
            payload = self.outer._parse_payload(kwargs)
            claim = payload.get("claim", {})
            heuristics = payload.get("rules_eval", rules_eval(claim))
            base_score = max(heuristics.get("score", 0.0), 0.05)
            line_factor = 0.15 * max(len(claim.get("lines", [])) - 1, 0)
            adjusted_score = base_score + 0.1 + line_factor
            if heuristics.get("signals"):
                adjusted_score = max(adjusted_score, 0.35)
            action = "manual_review" if adjusted_score >= 0.3 else "approve"
            return {
                "text": json.dumps(
                    {
                        "claim_id": claim.get("id", "unknown"),
                        "risk_score": round(min(adjusted_score, 1.0), 3),
                        "signals": heuristics.get("signals", []),
                        "action": action,
                    }
                )
            }

    def __init__(self) -> None:
        self._responses = EvalStubOpenAI._Responses(self)

    @property
    def responses(self) -> "EvalStubOpenAI._Responses":
        return self._responses

    def _parse_payload(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        messages = kwargs.get("input", [])
        for message in messages:
            if message.get("role") == "user":
                for block in message.get("content", []):
                    if block.get("type") == "text":
                        try:
                            return json.loads(block.get("text", "{}"))
                        except json.JSONDecodeError:
                            continue
        return {}


def load_tasks(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def run_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    client = TestClient(app)
    deps.get_openai_client.cache_clear()
    deps.get_manager_agent.cache_clear()
    deps.get_guard_chain.cache_clear()
    deps.get_handoff_publisher.cache_clear()
    stub = EvalStubOpenAI()
    app.dependency_overrides[deps.get_openai_client] = lambda: stub
    app.dependency_overrides[deps.get_manager_agent] = lambda: ManagerAgent(
        deps.get_agent_registry(),
        stub,
        ManagerConfig(hitl_threshold=deps.get_settings()["hitl_threshold"]),
    )
    results: List[Dict[str, Any]] = []
    for task in tasks:
        response = client.post("/score", json=task["claim"])
        payload = response.json()
        ok = response.status_code == 200
        result_payload = payload.get("result", {}) if ok else {}
        risk_score = result_payload.get("risk_score", 0) if isinstance(result_payload, dict) else 0
        handoff = bool(payload.get("handoff")) if ok else False
        guard = payload.get("guard") if ok else None
        passed = ok and risk_score >= task.get("expect_min_risk", 0)
        if "expect_handoff" in task:
            expected_handoff = bool(task["expect_handoff"])
            passed = passed and handoff == expected_handoff
        results.append(
            {
                "task": task["name"],
                "status": "ok" if ok else "error",
                "risk_score": risk_score,
                "handoff": handoff,
                "guard": guard,
                "passed": passed,
            }
        )
    app.dependency_overrides.pop(deps.get_openai_client, None)
    app.dependency_overrides.pop(deps.get_manager_agent, None)
    deps.get_openai_client.cache_clear()
    deps.get_manager_agent.cache_clear()
    deps.get_guard_chain.cache_clear()
    deps.get_handoff_publisher.cache_clear()
    return results


def write_report(path: Path, rows: List[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["task", "status", "risk_score", "handoff", "guard", "passed"],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run eval tasks against the /score API")
    parser.add_argument("--tasks", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    tasks = load_tasks(args.tasks)
    results = run_tasks(tasks)
    write_report(args.out, results)


if __name__ == "__main__":
    main()
