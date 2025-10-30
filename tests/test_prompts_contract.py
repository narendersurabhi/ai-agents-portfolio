from __future__ import annotations

from pathlib import Path

import yaml

AGENT_DIR = Path("configs/agents")


def test_agent_prompts_numbered_and_signaled() -> None:
    for path in AGENT_DIR.glob("*.agent.yaml"):
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        system_prompt: str = data.get("system_prompt", "")
        non_empty_lines = [line.strip() for line in system_prompt.splitlines() if line.strip()]
        assert non_empty_lines, f"system_prompt for {path.name} must not be empty"
        for line in non_empty_lines:
            assert line[0].isdigit(), f"Each prompt line must start with a number in {path.name}: {line}"
        completion_signal = data.get("completion_signal")
        assert completion_signal, f"completion_signal required for {path.name}"
        max_tool_calls = data.get("max_tool_calls")
        assert isinstance(max_tool_calls, int) and max_tool_calls > 0
