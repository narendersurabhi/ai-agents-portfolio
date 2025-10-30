from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Mapping

import yaml

from .base import AgentDefinition, BaseAgent
from . import tools as tool_module


@dataclass
class RegistryConfig:
    root: Path = Path("configs/agents")


class AgentRegistry:
    """Lazy loader for agent definitions declared in YAML."""

    def __init__(self, config: RegistryConfig | None = None) -> None:
        self.config = config or RegistryConfig()
        self._cache: Dict[str, BaseAgent] = {}

    def get(self, name: str) -> BaseAgent:
        if name not in self._cache:
            self._cache[name] = self._load_agent(name)
        return self._cache[name]

    def _load_agent(self, name: str) -> BaseAgent:
        path = self._config_path(name)
        with path.open("r", encoding="utf-8") as handle:
            data: Mapping[str, Any] = yaml.safe_load(handle)
        schema_path = Path(data["output_schema"])
        if not schema_path.is_absolute():
            schema_path = Path("schemas") / schema_path.name
        with schema_path.open("r", encoding="utf-8") as schema_file:
            schema = json.load(schema_file)
        tool_names = data.get("tools", [])
        available_tools = self._select_tools(tool_names)
        definition = AgentDefinition(
            name=data["name"],
            model=data["model"],
            system_prompt=data.get("system_prompt", ""),
            tool_names=tool_names,
            schema=schema,
        )
        return BaseAgent(definition, available_tools)

    def _select_tools(self, names: list[str]) -> Dict[str, Any]:
        module_dict = {name: getattr(tool_module, name) for name in dir(tool_module)}
        selected: Dict[str, Any] = {}
        for name in names:
            if name not in module_dict:
                raise KeyError(f"Tool '{name}' is not implemented in agents.tools")
            selected[name] = module_dict[name]
        return selected

    def _config_path(self, name: str) -> Path:
        filename = f"{name}.agent.yaml"
        path = self.config.root / filename
        if not path.exists():
            raise FileNotFoundError(f"Agent configuration not found: {path}")
        return path


__all__ = ["AgentRegistry", "RegistryConfig"]
