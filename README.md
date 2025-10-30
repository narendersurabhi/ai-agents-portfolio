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

Validates a claim payload against [`schemas/claim.json`](schemas/claim.json) and returns a triage result that matches [`schemas/triage_result.json`](schemas/triage_result.json).

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

Chains the investigator and explainer agents. The response conforms to [`schemas/explanation.json`](schemas/explanation.json) and includes a synthetic S3 PDF URL.

```bash
curl -s http://localhost:8080/explain \
  -H 'Content-Type: application/json' \
  -d '{"claim_id": "CLM-1"}'
```

### POST /feedback

Captures adjudication labels and stores them in DynamoDB when `FEEDBACK_TABLE` is configured, otherwise buffers in-memory.

```bash
curl -s http://localhost:8080/feedback \
  -H 'Content-Type: application/json' \
  -d '{"claim_id": "CLM-1", "label": "correct", "notes": "Matches policy."}'
```

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
