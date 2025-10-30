# AGENTS.md — Agentic Framework v2 (Guardrails + Orchestration + HITL)

Purpose: detect healthcare FWA with schema-first agents, observable flows, and explicit human-in-the-loop (HITL) handoffs.

## Repo map (authoritative)
```
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
```
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
