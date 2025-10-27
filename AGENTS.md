#### `AGENTS.md`
```markdown
# AGENTS.md

## Commands
- Install: `pip install -e .`
- Run CLI: `python -m src.app.cli ask "<question>"`
- Run API: `uvicorn src.app.api:app --port 8080`
- Tests: `pytest -q`
- Lint: `ruff check . && pyproject-fmt --check`

## Project conventions
- Source in `src/`. Tests in `tests/`.
- Agent configs in `agent_specs/*.yml` with `name`, `goals`, `tools`, `io_schema`.
- Tool adapters in `src/tools/` implement a pure function and a safety wrapper.
- Prompts live alongside agents as `PROMPT_*.md` strings in code for now.

## Branching
- Feature branches: `feat/<slug>`, `fix/<slug>`.
- PRs require passing CI and at least one review.

## How to extend
1. Add a new tool in `src/tools/<name>.py`.
2. Register it in `tooluse_agent.py`.
3. Add tests in `tests/test_tools.py`.
4. Update `agent_specs/tooluse.yml`.

## Change Log
- 2025-02-15: Updated `cdk/cdk-py/cdk_py/pipeline_stack.py` to grant the deploy CodeBuild project explicit `iam:PassRole` permissions for the `ai-agents` role when invoking App Runner, ensuring pipeline deployments can pass the access role successfully.
