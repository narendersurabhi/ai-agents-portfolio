from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Mapping

import jsonschema


class SchemaValidationError(ValueError):
    """Raised when agent output does not satisfy the declared schema."""


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    model: str
    system_prompt: str
    tool_names: Iterable[str]
    schema: Mapping[str, Any]


class BaseAgent:
    """Schema-first wrapper around the OpenAI Responses API."""

    def __init__(
        self,
        definition: AgentDefinition,
        tools: Mapping[str, Callable[..., Any]],
    ) -> None:
        self.definition = definition
        self._tools: Dict[str, Callable[..., Any]] = {
            name: tools[name] for name in definition.tool_names
        }

    @property
    def name(self) -> str:
        return self.definition.name

    @property
    def model(self) -> str:
        return self.definition.model

    @property
    def schema(self) -> Mapping[str, Any]:
        return self.definition.schema

    def enforce_schema(self, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        """Validate payload against the declared JSON schema."""

        try:
            jsonschema.validate(instance=payload, schema=self.schema)
        except jsonschema.ValidationError as exc:  # pragma: no cover - converted to ValueError
            raise SchemaValidationError(str(exc)) from exc
        return payload

    def run_tool(self, name: str, *args: Any, **kwargs: Any) -> Any:
        if name not in self._tools:
            available = ", ".join(sorted(self._tools)) or "<none>"
            raise KeyError(f"Tool '{name}' is not registered for agent '{self.name}'. Available: {available}")
        return self._tools[name](*args, **kwargs)

    def build_messages(self, payload: Mapping[str, Any]) -> List[Dict[str, Any]]:
        return [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": self.definition.system_prompt.strip(),
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(payload, sort_keys=True),
                    }
                ],
            },
        ]

    def _extract_response_text(self, response: Any) -> str:
        # The OpenAI Responses API returns an object with an ``output`` list where each entry
        # contains ``content`` chunks. The tests mock a simpler dict. This extractor accepts both.
        if response is None:
            raise ValueError("Agent call returned no response")

        if isinstance(response, str):
            return response

        # Dict-based mocks
        if isinstance(response, dict):
            if "output" in response:
                return self._extract_from_output(response["output"])
            if "content" in response:
                return self._extract_from_output(response["content"])
            if "text" in response:
                return str(response["text"])

        # Objects from the SDK
        output = getattr(response, "output", None)
        if output is not None:
            return self._extract_from_output(output)

        raise ValueError("Unsupported response format from OpenAI client")

    def _extract_from_output(self, output: Any) -> str:
        chunks: List[str] = []
        if isinstance(output, list):
            for item in output:
                if isinstance(item, dict):
                    content = item.get("content")
                    if isinstance(content, list):
                        for chunk in content:
                            if isinstance(chunk, dict):
                                if chunk.get("type") in {"output_text", "text"}:
                                    text = chunk.get("text")
                                    if text:
                                        chunks.append(str(text))
                    elif isinstance(content, str):
                        chunks.append(content)
                elif isinstance(item, str):
                    chunks.append(item)
        elif isinstance(output, str):
            chunks.append(output)
        if not chunks:
            raise ValueError("OpenAI response did not contain textual content")
        return "".join(chunks)

    def run(self, client: Any, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        response = client.responses.create(
            model=self.model,
            input=self.build_messages(payload),
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": f"{self.name}_output",
                    "schema": self.schema,
                },
            },
        )
        text = self._extract_response_text(response)
        data = json.loads(text)
        return self.enforce_schema(data)


__all__ = ["AgentDefinition", "BaseAgent", "SchemaValidationError"]
