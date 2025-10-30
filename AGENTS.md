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
- Region: us-east-2
- CodePipeline → CodeBuild → ECR → App Runner
- Deploy uses role/AppRunnerEcrAccessRole. No self-pass of role/ai-agents.

## Secrets
- OPENAI_API_KEY, AWS_REGION at runtime.
- No real PHI. Mask sensitive data in logs.

## DoD (per PR)
- Tests green. Schemas enforced. Evals non-degrading.
- README/API examples updated if changed.
- Least-privileged IAM only.

## Task queue
1) Implement /score (rules_eval + feature_stats + triage agent).
2) Implement /explain (investigator → explainer, PDF to S3).
3) Add evals: upcoding_units, impossible_combo, high_freq_modifier.
4) Observability: structured logs, p95 latency, token cost.
5) Cost controls: model choice, max tokens, streaming by default.

## Known pitfalls
- iam:PassRole must target only role/AppRunnerEcrAccessRole.
- Require ACCESS_ROLE_ARN env; do not fallback to role/ai-agents.
- Keep schemas strict and versioned.

## Change log
- Added observability middleware with structured JSON logs, rolling p95 latency, and token cost tracking plus streaming defaults for agent calls.
- Scaffolded schema-first FastAPI runtime with `/score`, `/explain`, and `/feedback` routes using strict JSON schema enforcement.
- Added agent registry, base runtime, and tool stubs alongside triage/investigator/explainer YAML configurations.
- Introduced evaluation harness, unit tests, and README documentation covering the new APIs.
- Added GuardChain (PII redaction, prompt-injection, relevance) with manager-orchestrated flows for `/score` and `/explain`, envelope responses, and HITL escalations.
- Implemented SNS-backed handoff publisher, feedback handoff propagation, numbered prompts with completion signals, and extended tests/evals for guard coverage.
- Documented end-to-end request flow with guard chain, manager orchestration, and HITL handoff diagram in README.
- Fixed README request-flow Mermaid diagram labels to render on GitHub without parse errors.
