from __future__ import annotations

import json
from typing import Any

import pytest

from agents.base import AgentDefinition, BaseAgent, SchemaValidationError


class DummyClient:
    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload
        self.last_request: dict[str, Any] | None = None

    class _Responses:
        def __init__(self, outer: "DummyClient") -> None:
            self.outer = outer

        def create(self, **kwargs: Any) -> dict[str, Any]:
            self.outer.last_request = kwargs
            return {"text": json.dumps(self.outer.payload)}

    @property
    def responses(self) -> "DummyClient._Responses":
        return DummyClient._Responses(self)


def test_enforce_schema_validates_output():
    schema = {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}
    definition = AgentDefinition(
        name="test",
        model="gpt-5",
        system_prompt="",
        tool_names=[],
        schema=schema,
    )
    agent = BaseAgent(definition, {})
    with pytest.raises(SchemaValidationError):
        agent.enforce_schema({"value": "not-int"})


def test_run_invokes_openai_with_schema_format():
    schema = {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}
    definition = AgentDefinition(
        name="test",
        model="gpt-5",
        system_prompt="Use schema",
        tool_names=["echo"],
        schema=schema,
    )

    def echo_tool(x: Any) -> Any:
        return x

    agent = BaseAgent(definition, {"echo": echo_tool})
    client = DummyClient({"value": 3})

    result = agent.run(client, {"foo": "bar"})
    assert result == {"value": 3}
    assert client.last_request is not None
    assert client.last_request["response_format"]["json_schema"]["schema"] == schema


def test_run_tool_dispatch():
    schema = {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}
    definition = AgentDefinition(
        name="test",
        model="gpt-5",
        system_prompt="",
        tool_names=["double"],
        schema=schema,
    )

    def double(x: int) -> int:
        return x * 2

    agent = BaseAgent(definition, {"double": double})
    assert agent.run_tool("double", 3) == 6
    with pytest.raises(KeyError):
        agent.run_tool("missing")
