from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional

import jsonschema

from observability import get_metrics, log_event


class SchemaValidationError(ValueError):
    """Raised when agent output does not satisfy the declared schema."""


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    model: str
    system_prompt: str
    tool_names: Iterable[str]
    schema: Mapping[str, Any]
    completion_signal: Optional[str] = None
    max_tool_calls: Optional[int] = None


class BaseAgent:
    """Schema-first wrapper around the OpenAI Responses API."""

    MAX_OUTPUT_TOKENS = 512
    TEMPERATURE = 0.0

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
            raise KeyError(
                f"Tool '{name}' is not registered for agent '{self.name}'. Available: {available}"
            )
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

    def _response_options(self) -> Dict[str, Any]:
        return {
            "stream": True,
            "max_output_tokens": self.MAX_OUTPUT_TOKENS,
            "temperature": self.TEMPERATURE,
        }

    def run(self, client: Any, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        log_event("agent.call.start", agent=self.name, model=self.model)
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
            **self._response_options(),
        )
        text, usage_payload = self._parse_response(response)
        if self.definition.completion_signal and self.definition.completion_signal not in text:
            log_event(
                "agent.termination.signal_missing",
                agent=self.name,
                expected=self.definition.completion_signal,
            )
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            log_event(
                "agent.output.invalid_json",
                agent=self.name,
                model=self.model,
                error=str(exc),
            )
            raise SchemaValidationError("Agent output was not valid JSON") from exc
        if not isinstance(data, Mapping):
            log_event(
                "agent.output.invalid_type",
                agent=self.name,
                model=self.model,
                received_type=type(data).__name__,
            )
            raise SchemaValidationError("Agent output must be a JSON object")

        result = self.enforce_schema(data)
        usage = self._normalize_usage(usage_payload)
        if usage:
            metrics = get_metrics()
            summary = metrics.record_tokens(
                self.name,
                self.model,
                prompt_tokens=usage.get("prompt_tokens", 0),
                completion_tokens=usage.get("completion_tokens", 0),
                total_tokens=usage.get("total_tokens"),
            )
            log_payload = summary.copy()
            log_payload["agent"] = self.name
            log_event("agent.tokens", **log_payload)
        log_event("agent.call.complete", agent=self.name, model=self.model)
        return result

    def _parse_response(self, response: Any) -> tuple[str, Any]:
        if isinstance(response, dict) or hasattr(response, "output"):
            text = self._extract_response_text(response)
            usage = self._extract_usage(response)
            return text, usage
        if self._is_streaming_response(response):
            return self._consume_stream(response)
        raise ValueError("Unsupported response type from OpenAI client")

    def _is_streaming_response(self, response: Any) -> bool:
        return hasattr(response, "__iter__") and not isinstance(response, (str, bytes, dict))

    def _consume_stream(self, stream: Iterable[Any]) -> tuple[str, Any]:
        text_parts: List[str] = []
        final_payload: Any = None
        for event in stream:
            event_type = getattr(event, "type", None)
            if isinstance(event, dict):
                event_type = event.get("type")
            if event_type == "response.output_text.delta":
                delta = getattr(event, "delta", None)
                if isinstance(event, dict):
                    delta = event.get("delta", delta)
                if delta:
                    text_parts.append(str(delta))
            elif event_type in {"response.completed", "response.completed_successfully"}:
                final_payload = getattr(event, "response", None)
                if isinstance(event, dict):
                    final_payload = event.get("response", final_payload)
                break
        usage = self._extract_usage(final_payload)
        if final_payload and not text_parts:
            try:
                return self._extract_response_text(final_payload), usage
            except ValueError:
                pass
        return "".join(text_parts), usage

    def _extract_usage(self, payload: Any) -> Any:
        if payload is None:
            return None
        if isinstance(payload, dict):
            return payload.get("usage")
        return getattr(payload, "usage", None)

    def _normalize_usage(self, usage: Any) -> Dict[str, int] | None:
        if usage is None:
            return None

        def _lookup(*keys: str) -> int:
            for key in keys:
                if isinstance(usage, dict) and key in usage:
                    return int(usage[key] or 0)
                value = getattr(usage, key, None)
                if value is not None:
                    return int(value or 0)
            return 0

        prompt_tokens = _lookup("prompt_tokens", "input_tokens")
        completion_tokens = _lookup("completion_tokens", "output_tokens")
        total_tokens = _lookup("total_tokens")
        if not total_tokens:
            total_tokens = prompt_tokens + completion_tokens
        if not any([prompt_tokens, completion_tokens, total_tokens]):
            return None
        return {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
        }


__all__ = ["AgentDefinition", "BaseAgent", "SchemaValidationError"]
