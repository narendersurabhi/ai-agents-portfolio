# AGENTS.md — Codex Agent Playbook

Purpose: enable autonomous PRs that add or improve agentic AI features for healthcare FWA detection and resume tooling, with strict safety, tests, and CI/CD to AWS App Runner.

## Repo map (authoritative)
```
app/                  # FastAPI app (HTTP API, streaming)
  main.py
  deps.py
  routes/
    score.py          # /score (triage)
    explain.py        # /explain (investigate+explain)
    feedback.py       # /feedback
agents/
  base.py             # BaseAgent, Tool wiring, schema enforcement
  registry.py         # YAML loader
  tools.py            # tool handlers (S3, rules_eval, feature_stats, etc.)
configs/
  agents/
    triage.agent.yaml
    investigator.agent.yaml
    explainer.agent.yaml
schemas/              # JSON Schema Draft 2020-12
  claim.json
  triage_result.json
  investigation.json
  explanation.json
evals/
  tasks.yaml          # eval scenarios
  scorer.py           # scoring and report
tests/
  test_schemas.py
  test_runtime.py
  test_agents.py
docker/
  Dockerfile
buildspec.yml
cdk/
  cdk-py/             # CDK pipeline (CodePipeline → CodeBuild → App Runner)
README.md
AGENTS.md
```

## Commands
- Install: `pip install -r requirements.txt`
- Dev API: `uvicorn app.main:app --reload --port 8080`
- Tests: `pytest -q`
- Evals: `python -m evals.scorer --tasks evals/tasks.yaml --out evals/report.csv`
- Lint/format: `ruff check . && ruff format --check .`

## Agent contracts
- Specs in `configs/agents/*.agent.yaml`.
- Each must reference a JSON schema under `schemas/`.
- Outputs must validate. On failure: HTTP 400 `schema_error`.

YAML example:
```yaml
name: triage
model: gpt-5
system_prompt: |
  Score fraud risk 0..1; cite rules and peer deviations. Output triage_result schema.
tools: [rules_eval, feature_stats, provider_history]
output_schema: schemas/triage_result.json
```

## Tools
Pure functions in `agents/tools.py`. Allowed by default:
- s3_get, s3_put
- rules_eval, feature_stats, provider_history
- search_policy, render_pdf

## HTTP API
- POST /score → claim.json → triage_result.json
- POST /explain → {claim_id} → explanation.json
- POST /feedback → {claim_id,label,notes} → {ok:true}
Streaming endpoint exists at `/v1/agents/{agent}/chat` for long calls.

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
