# Code Review Summary

## Overall assessment
The repository delivers a schema-first, guard-railed FastAPI service for orchestrating multiple LLM agents. The codebase is well-covered by tests (`pytest` passes locally) and leans on explicit JSON Schema validation and token/latency telemetry, which provides a strong baseline for productionizing agent workflows.

## Highlights
- **Robust schema enforcement** – `BaseAgent` ensures every agent output validates against its declared JSON schema and normalizes streaming vs. non-streaming responses before logging metrics, reducing the chance of silent contract drift.【F:agents/base.py†L24-L155】
- **Built-in observability** – The global middleware instruments every HTTP call with latency histograms and structured JSON logs, giving immediate insight into route performance and health-check status.【F:app/main.py†L9-L49】【F:observability.py†L16-L119】
- **Deterministic synthetic tooling** – Helper tools (`rules_eval`, `feature_stats`, `provider_history`) create reproducible signals for evaluations and tests, while still mimicking realistic fraud-detection heuristics.【F:agents/tools.py†L13-L66】

## Risks & recommendations
1. **HITL configuration drift** – The docs call for a default HITL threshold of 0.6 controlled by `HITL_THRESHOLD`, but the code hard-codes `DEFAULT_HITL_THRESHOLD = 0.85` and reads `HITL_RISK_THRESHOLD`. Aligning the environment variable name and default value would prevent surprises in production rollouts.【F:AGENTS.md†L41-L51】【F:app/deps.py†L21-L44】
2. **Guard chain ordering mismatch** – The guard chain currently instantiates the PII redactor before relevance and prompt-injection checks, while the documented pattern wraps logging with PII masking and runs the other guards pre-LLM. Consider keeping redaction in the logger path and executing relevance/prompt-injection guards first to minimize unnecessary processing and to meet documented behavior.【F:AGENTS.md†L29-L39】【F:app/deps.py†L46-L57】
3. **Unused HITL threshold** – `ManagerAgent` exposes a configurable `hitl_threshold`, yet the flow implementations never consult it to decide on human handoff. Surfacing the score threshold evaluation inside `_run_score` (and propagating handoff context) would complete the intended HITL loop.【F:agents/manager.py†L14-L67】

## Suggested next steps
- Harmonize environment variables and defaults for HITL thresholds, plus extend tests to cover the configuration surface.
- Refactor guard wiring so the chain order and behavior match the documented architecture.
- Introduce HITL decision logic (and tests) within `ManagerAgent` to drive actual handoff triggers based on risk scores or guard outcomes.
