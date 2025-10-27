![Pipeline](https://img.shields.io/badge/CodePipeline-AiAgentsPortfolio-blue)
![Build](https://img.shields.io/badge/CodeBuild-docker-green)
![CodePipeline](https://img.shields.io/badge/CodePipeline-AiAgentsPortfolio-blue)
![Pipeline](https://img.shields.io/badge/CodePipeline-active-success)
![Build](https://img.shields.io/badge/CodeBuild-docker-green)
![CI](https://github.com/narendersurabhi/ai-agents-portfolio/actions/workflows/ci.yml/badge.svg) 
![Deploy](https://github.com/narendersurabhi/ai-agents-portfolio/actions/workflows/deploy.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)

# AI Agents Portfolio

Production-grade demos of three agent types:
1) Retrieval Agent: grounded Q&A over local docs.
2) Orchestration Agent: multi-step planner with tool routing.
3) Tool-Use Agent: executes safe functions (search, S3, vector store).

## Quickstart
```bash
cp .env.example .env   # set OPENAI_API_KEY or provider of choice
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m src.pipelines.ingest_docs --path data/docs
python -m src.pipelines.build_index --src data/docs --out data/vector_index
python -m src.app.cli ask "Summarize the docs and list key risks."
