from __future__ import annotations

import json
from typing import Any, Iterable

import pytest

from agents.base import AgentDefinition, BaseAgent, SchemaValidationError
from observability import get_metrics


@pytest.fixture(autouse=True)
def reset_metrics() -> Iterable[None]:
    metrics = get_metrics()
    metrics.reset()
    yield
    metrics.reset()


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
        return type(self)._Responses(self)


class StreamingClient:
    def __init__(self, events: list[dict[str, Any]]) -> None:
        self._events = events
        self.last_request: dict[str, Any] | None = None

    class _Responses:
        def __init__(self, outer: "StreamingClient") -> None:
            self.outer = outer

        def create(self, **kwargs: Any) -> Iterable[dict[str, Any]]:
            self.outer.last_request = kwargs
            return iter(self.outer._events)

    @property
    def responses(self) -> "StreamingClient._Responses":
        return StreamingClient._Responses(self)


class InvalidJSONClient(DummyClient):
    class _Responses(DummyClient._Responses):
        def create(self, **kwargs: Any) -> dict[str, Any]:
            self.outer.last_request = kwargs
            return {"text": "not-json"}


def test_enforce_schema_validates_output() -> None:
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


def test_run_invokes_openai_with_schema_format() -> None:
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
    assert client.last_request.get("stream") is True
    assert client.last_request.get("max_output_tokens") == BaseAgent.MAX_OUTPUT_TOKENS


def test_run_tool_dispatch() -> None:
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


def test_run_raises_for_invalid_json_output() -> None:
    schema = {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}
    definition = AgentDefinition(
        name="test",
        model="gpt-5",
        system_prompt="",
        tool_names=[],
        schema=schema,
    )
    agent = BaseAgent(definition, {})
    client = InvalidJSONClient({"value": 1})

    with pytest.raises(SchemaValidationError):
        agent.run(client, {"foo": "bar"})


def test_run_handles_streaming_events_and_records_tokens() -> None:
    schema = {"type": "object", "properties": {"value": {"type": "integer"}}, "required": ["value"]}
    definition = AgentDefinition(
        name="test",
        model="gpt-5",
        system_prompt="",
        tool_names=[],
        schema=schema,
    )
    agent = BaseAgent(definition, {})
    events = [
        {"type": "response.output_text.delta", "delta": '{"value": '},
        {"type": "response.output_text.delta", "delta": "7}"},
        {
            "type": "response.completed",
            "response": {
                "output": [
                    {
                        "content": [
                            {
                                "type": "output_text",
                                "text": '{"value": 7}',
                            }
                        ]
                    }
                ],
                "usage": {"input_tokens": 5, "output_tokens": 7},
            },
        },
    ]
    client = StreamingClient(events)

    result = agent.run(client, {"foo": "bar"})
    assert result == {"value": 7}

    metrics = get_metrics().snapshot()
    assert metrics["token_usage"]["test"]["total_tokens"] == 12
    assert metrics["token_usage"]["test"]["prompt_tokens"] == 5
