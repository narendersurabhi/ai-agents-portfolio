# AGENTS.md — Agentic Framework v2 (Guardrails + Orchestration + HITL)

Purpose: detect healthcare FWA with schema-first agents, observable flows, and explicit human-in-the-loop (HITL) handoffs.

## Repo map (authoritative)
app/
  main.py
  deps.py                 # clients, guard chain, settings
  routes/
    score.py             # /score  → manager(flow="score")
    explain.py           # /explain → manager(flow="explain")
    feedback.py          # /feedback
agents/
  base.py                # BaseAgent, schema enforcement, tool router
  registry.py            # YAML loader
  tools.py               # rules_eval, feature_stats, provider_history, search_policy, render_pdf, s3_get/s3_put
  manager.py             # ManagerAgent.run(flow)
  guards/
    relevance.py
    prompt_injection.py
    pii_redactor.py
configs/
  agents/
    triage.agent.yaml
    investigator.agent.yaml
    explainer.agent.yaml
schemas/
  claim.json
  triage_result.json
  investigation.json
  explanation.json
  feedback.json
evals/
  tasks.yaml
  scorer.py
tests/
  test_schemas.py
  test_runtime.py
  test_agents.py
  test_guards.py
  test_prompts_contract.py

## Orchestration pattern
Manager-orchestrated flows. Single entry. Explicit termination and handoff.
- score: guards → tools → triage agent → validate → maybe HITL.
- explain: guards → investigator agent → explainer agent (+ render_pdf) → validate → maybe HITL.
Termination: each agent uses `completion_signal: "<END_OF_TASK>"` for tests only. Output is pure JSON.

## Guardrails
- relevance: reject off-scope inputs.
- prompt_injection: detect jailbreak markers; deny or strip.
- pii_redactor: mask phone, SSN, MRN in logs only.
Wiring: `GuardChain([relevance, prompt_injection])` runs pre-LLM. `pii_redactor` wraps logger.
On guard trip: HTTP 422 with `{reason, handoff:"human_review"}`. Optional SNS notify.

## Human-in-the-loop (HITL)
Env: `HITL_THRESHOLD` (default 0.6). If `risk_score >= threshold` or guard trips → `{handoff:"human_review"}`.
`/feedback` accepts `{claim_id,label,notes,handoff}`. Store to DynamoDB if configured, else memory.
Optional: `SNS_HANDOFF_TOPIC_ARN` to publish events.

## Agent contracts
YAML lives in `configs/agents/*.agent.yaml`. Reference JSON Schemas in `schemas/`. Use numbered, schema-first prompts.

Example `triage.agent.yaml`
```yaml
name: triage
model: gpt-5
max_tool_calls: 4
completion_signal: "<END_OF_TASK>"
system_prompt: |
  1) Read the claim JSON.
  2) Call tools: rules_eval → feature_stats → provider_history.
  3) Output JSON that validates schemas/triage_result.json only.
  4) If validation fails, emit {"schema_error":"<reason>"} and stop.
  5) No PHI in output. Calibrate: 0–0.2 approve, 0.2–0.6 queue_review, 0.6–1.0 auto_deny unless contradicting evidence.
tools: [rules_eval, feature_stats, provider_history]
output_schema: schemas/triage_result.json
````

Example `explainer.agent.yaml`

```yaml
name: explainer
model: gpt-5
completion_signal: "<END_OF_TASK>"
system_prompt: |
  1) Read investigation JSON.
  2) Synthesize a concise reviewer note with citations.
  3) Call render_pdf to create a one-page PDF.
  4) Output schemas/explanation.json only.
tools: [render_pdf]
output_schema: schemas/explanation.json
```

## HTTP API

* POST /score → body matches `schemas/claim.json` → returns `schemas/triage_result.json` or 422 with HITL.
* POST /explain → body `{claim_id}` → returns `schemas/explanation.json` (+ `report_url`).
* POST /feedback → body `schemas/feedback.json` → `{ok:true}`.
  Streaming: `/v1/agents/{agent}/chat` for long tasks.

## Evals

`evals/tasks.yaml`: `upcoding_units`, `impossible_combo`, `high_freq_modifier`, `off_topic_query`, `prompt_injection_string`, `phi_present`.
`evals/scorer.py` metrics: `schema_valid_rate`, `guard_trip_rate`, `hitl_rate@threshold`, `latency_p95`.

## CI/CD invariants

Region `us-east-2`. CodePipeline → CodeBuild → ECR → App Runner. Deploy uses `role/AppRunnerEcrAccessRole`. Build outputs `image.json`.

## Secrets and config

Required: `OPENAI_API_KEY`, `AWS_REGION`. Optional: `SNS_HANDOFF_TOPIC_ARN`, `HITL_THRESHOLD`, `S3_BUCKET_AGENTS`. No real PHI.

## Definition of Done

Tests and evals pass. Schemas enforced. README shows orchestration and HITL. No IAM broadening. Region unchanged.

## Change log

2025-10-30: v2 adds manager orchestration, guardrails, HITL, termination criteria, and safety evals.

```

# Codex task prompt
```

You are a repository-maintenance agent. Implement Agentic Framework v2 per AGENTS.md at repo root. Open a focused PR that adds guardrails, manager orchestration, termination criteria, and HITL plumbing. Keep CI green.

AUTHORITATIVE SPEC

* Use AGENTS.md — Agentic Framework v2. Do not diverge.

GOALS

1. Add guards (relevance, prompt_injection, pii_redactor) and wire GuardChain in FastAPI deps and routes.
2. Add ManagerAgent with flows: score, explain. Routes call manager.
3. Update agent YAMLs with numbered schema-first prompts, completion_signal, max_tool_calls.
4. Enforce HITL: threshold env, return handoff on high risk or guard trip, publish SNS if configured.
5. Extend evals and tests. Keep CI/CD invariants.

CONSTRAINTS

* Region us-east-2. No IAM or pipeline drift. No real PHI. Pure functions for tools.
* Enforce JSON Schema on all agent outputs. On failure: HTTP 400 with schema_error.

IMPLEMENTATION STEPS

* Create `agents/guards/{relevance.py,prompt_injection.py,pii_redactor.py}`.
* Add `agents/manager.py` with `run(flow)` implementing the two flows.
* Edit YAMLs under `configs/agents/` as in AGENTS.md v2. Keep model `gpt-5`.
* Update `app/deps.py` to construct `GuardChain` and expose `get_guard_chain()`.
* Update `app/routes/{score.py,explain.py}` to call guards pre-LLM and enforce schema post-LLM. Add HITL threshold logic.
* Update `/feedback` to accept `{handoff}` and publish to `SNS_HANDOFF_TOPIC_ARN` when set.
* Add tests: `tests/test_guards.py`, `tests/test_prompts_contract.py`. Update existing tests.
* Update `evals/tasks.yaml` and `evals/scorer.py` to include guard/HITL metrics.
* Update README: orchestration diagram and HITL behavior. Do not edit CDK.

QUALITY GATES

* `pytest -q` passes. `ruff check .` passes. Evals produce non-degrading CSV.
* No changes to IAM or region. App Runner deploy unchanged.

PR TEMPLATE
Title: feat(agents): add manager orchestration, guardrails, and HITL (v2)
Body: problem, approach, files changed, schema updates, tests/evals, risks, rollback.

RUN LOCALLY BEFORE PR

* `pip install -r requirements.txt`
* `pytest -q && ruff check .`
* `python -m evals.scorer --tasks evals/tasks.yaml --out evals/report.csv`
* `uvicorn app.main:app --reload --port 8080`

```
::contentReference[oaicite:0]{index=0}
```
