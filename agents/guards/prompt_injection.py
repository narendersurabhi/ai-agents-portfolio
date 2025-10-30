from __future__ import annotations

import json
from typing import Any, Iterable, Mapping

from . import GuardDecision

_SUSPICIOUS_PHRASES: tuple[str, ...] = (
    "ignore previous instructions",
    "override system",
    "exfiltrate",
    "delete all logs",
    "run arbitrary code",
)


def _flatten_strings(payload: Mapping[str, Any]) -> Iterable[str]:
    stack: list[Any] = [payload]
    while stack:
        item = stack.pop()
        if isinstance(item, Mapping):
            stack.extend(item.values())
        elif isinstance(item, list):
            stack.extend(item)
        elif isinstance(item, str):
            yield item


class PromptInjectionGuard:
    name = "prompt_injection"

    def run(
        self,
        payload: Mapping[str, Any],
        *,
        context: Mapping[str, Any] | None = None,
    ) -> GuardDecision:
        del context  # unused
        text_blob = "\n".join(_flatten_strings(payload)).lower()
        serialized = json.dumps(payload, sort_keys=True).lower()
        combined = f"{text_blob}\n{serialized}"
        for phrase in _SUSPICIOUS_PHRASES:
            if phrase in combined:
                return GuardDecision(
                    handoff=True,
                    reason=f"Detected prompt injection phrase: '{phrase}'",
                )
        return GuardDecision()


__all__ = ["PromptInjectionGuard"]
