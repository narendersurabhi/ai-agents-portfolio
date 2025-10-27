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
