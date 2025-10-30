![Pipeline](https://img.shields.io/badge/CodePipeline-AiAgentsPortfolio-blue)
![Build](https://img.shields.io/badge/CodeBuild-docker-green)
![CodePipeline](https://img.shields.io/badge/CodePipeline-AiAgentsPortfolio-blue)
![Pipeline](https://img.shields.io/badge/CodePipeline-active-success)
![Build](https://img.shields.io/badge/CodeBuild-docker-green)
![CI](https://github.com/narendersurabhi/ai-agents-portfolio/actions/workflows/ci.yml/badge.svg) 
![Deploy](https://github.com/narendersurabhi/ai-agents-portfolio/actions/workflows/deploy.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)

# AI Agents Portfolio

Production-grade demos of schema-first agents for healthcare claim triage, investigation, and explanation.

## Agentic FWA API

The FastAPI service in `app/` exposes JSON-schema enforced endpoints. Spin it up locally:

```bash
uvicorn app.main:app --reload --port 8080
```

### POST /score

Runs the claim payload through the guard chain (PII redaction → prompt-injection detection → relevance) before invoking the manager agent. The manager orchestrates feature enrichment and the triage agent, returning an envelope:

```json
{
  "handoff": false,
  "result": { ...triage_result schema... },
  "reason": "optional human-in-loop rationale"
}
```

If the guard chain trips, or if the triage output exceeds the configured HITL threshold / requests manual review, the endpoint flips `handoff` to `true` and publishes an SNS notification when `SNS_HANDOFF_TOPIC_ARN` is set.

```bash
curl -s http://localhost:8080/score \
  -H 'Content-Type: application/json' \
  -d @- <<'JSON'
{
  "id": "CLM-1",
  "member": {"id": "M-1", "dob": "1980-01-01", "plan_id": "P-1"},
  "provider": {"npi": "1234567890", "name": "Clinic"},
  "dos": "2024-01-01",
  "place": "office",
  "amount": 250.0,
  "lines": [{"cpt": "99213", "units": 2, "charge": 250.0, "dx": ["Z00.00"]}]
}
JSON
```

### POST /explain

Uses the same guard chain before handing off to the manager flow that calls investigator → explainer. The response mirrors the `/score` envelope and includes the validated explanation payload plus the underlying investigation context.

```bash
curl -s http://localhost:8080/explain \
  -H 'Content-Type: application/json' \
  -d '{"claim_id": "CLM-1"}'
```

### POST /feedback

Captures adjudication labels and optional `handoff` state. When `FEEDBACK_TABLE` is configured the entry is written to DynamoDB; otherwise it is buffered in-memory. If `handoff` is true the SNS publisher is invoked so downstream reviewers receive the escalation event.

```bash
curl -s http://localhost:8080/feedback \
  -H 'Content-Type: application/json' \
  -d '{"claim_id": "CLM-1", "label": "correct", "notes": "Matches policy."}'
```


### Request flow overview

The FastAPI stack in [`app/main.py`](app/main.py) wires the observability middleware before delegating to the individual routers in [`app/routes/`](app/routes). Requests are validated against JSON Schemas, enriched with deterministic tooling, executed through schema-constrained OpenAI agents, and finally returned with any side effects (PDF rendering or feedback persistence) applied. The following diagram highlights how each endpoint is orchestrated end-to-end:

```mermaid
flowchart TD
    subgraph HTTP Layer
        Client((Client)) -->|POST /score| Observability
        Client -->|POST /explain| Observability
        Client -->|POST /feedback| Observability
        Observability[[app.main: observability_middleware]] --> RouterSelection[[FastAPI router dispatch]]
        RouterSelection --> ScoreRoute[[app/routes/score.py]]
        RouterSelection --> ExplainRoute[[app/routes/explain.py]]
        RouterSelection --> FeedbackRoute[[app/routes/feedback.py]]
    end

    subgraph Score Flow
        ScoreRoute -->|validate| ClaimSchema[[schemas/claim.json]]
        ScoreRoute -->|compose payload| ScoreTools[[rules_eval\nfeature_stats\nprovider_history]]
        ScoreTools --> ScoreRoute
        ScoreRoute -->|run triage agent| TriageAgent[[configs/agents/triage.agent.yaml]]
        TriageAgent -->|responses.create| OpenAI[(OpenAI Responses API)]
        TriageAgent -->|enforce| TriageSchema[[schemas/triage_result.json]]
        TriageAgent --> ScoreResponse{{Triage result}}
    end

    subgraph Explain Flow
        ExplainRoute -->|load investigator| Investigator[[configs/agents/investigator.agent.yaml]]
        Investigator -->|responses.create| OpenAI
        Investigator --> Investigation{{Investigation JSON}}
        ExplainRoute --> Investigation
        ExplainRoute -->|load explainer| Explainer[[configs/agents/explainer.agent.yaml]]
        Explainer -->|responses.create| OpenAI
        Explainer --> Explanation{{Explanation JSON}}
        Explanation -->|attach report| RenderPDF[[agents.tools.render_pdf]]
        RenderPDF --> Explanation
        Explainer -->|enforce| ExplanationSchema[[schemas/explanation.json]]
    end

    subgraph Feedback Flow
        FeedbackRoute[[app/routes/feedback.py]] --> FeedbackRepo[[app.deps.FeedbackRepository]]
        FeedbackRepo -->|put| Dynamo[(DynamoDB Table or in-memory buffer)]
        FeedbackRepo --> FeedbackResponse{{Feedback ACK JSON}}
    end

    ScoreResponse -->|HTTP 200/400| Client
    Explanation -->|HTTP 200/400| Client
    FeedbackResponse -->|HTTP 200| Client
```

The feedback acknowledgment payload is a minimal JSON body of `{"ok": true}`.

**Key behaviors**

* **Schema enforcement** – Each route validates inputs and outputs via the JSON Schemas in `schemas/`, surfacing a `400` with `schema_error` when enforcement fails.
* **Tooling and agents** – Deterministic helpers in [`agents/tools.py`](agents/tools.py) feed structured context into the agents defined under `configs/agents/`, which execute through the `BaseAgent` wrapper in [`agents/base.py`](agents/base.py).
* **Observability** – The middleware in `app/main.py` captures latency metrics and structured events for both successful and error paths, ensuring downstream monitoring captures guardrail outcomes and token spend.


### Observability & Cost Controls

The API emits structured JSON logs via `observability.log_event` with request metadata, p95 latency, and agent token usage summaries.
The `observability.Metrics` singleton keeps a rolling window of the last 100 durations per route and aggregates prompt/completion token
counts per agent to estimate dollar spend using the pricing table in `observability.MODEL_PRICING`.

* Inspect structured logs while the server runs to monitor latency and schema enforcement outcomes.
* Query the in-memory metrics snapshot (`observability.get_metrics().snapshot()`) for dashboards or health endpoints.
* Responses are requested in streaming mode with a `max_output_tokens` cap (512 by default) to bound model cost while still providing
schema-conformant JSON payloads.

### Manager Orchestration, Guardrails, and HITL

* `agents/manager.py` coordinates the score and explain flows, invoking the specialist agents while enforcing schema validation on every hop.
* The `GuardChain` (PII redactor → prompt-injection detector → relevance check) runs inside `app/deps.get_guard_chain` and is applied before any model call.
* Human-in-the-loop escalation triggers whenever the guard chain blocks a request, the triage score crosses `HITL_RISK_THRESHOLD` (default `0.85`), or downstream agents recommend manual review / denial.
* Optional environment variables:
  * `HITL_RISK_THRESHOLD` – override the risk-score cutoff for automatic handoff.
  * `SNS_HANDOFF_TOPIC_ARN` – publish escalation events to an SNS topic for reviewer notification.

### Evaluations

Offline smoke tests for `/score` live at [`evals/tasks.yaml`](evals/tasks.yaml). Generate a CSV report:

```bash
python -m evals.scorer --tasks evals/tasks.yaml --out evals/report.csv
```

## Quickstart
```bash
cp .env.example .env   # set OPENAI_API_KEY or provider of choice
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m src.pipelines.ingest_docs --path data/docs
python -m src.pipelines.build_index --src data/docs --out data/vector_index
python -m src.app.cli ask "Summarize the docs and list key risks."
