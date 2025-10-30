from __future__ import annotations

import re
from copy import deepcopy
from typing import Any, Mapping

from . import GuardDecision

_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
_DIGIT_BLOCK_RE = re.compile(r"\b\d{9,}\b")


def _redact_string(value: str) -> str:
    result = _EMAIL_RE.sub("[redacted-email]", value)
    result = _SSN_RE.sub("[redacted-ssn]", result)
    result = _DIGIT_BLOCK_RE.sub("[redacted-id]", result)
    return result


def _sanitize(value: Any) -> Any:
    if isinstance(value, str):
        return _redact_string(value)
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, Mapping):
        return {key: _sanitize(val) for key, val in value.items()}
    return value


class PIIRedactorGuard:
    name = "pii_redactor"

    def run(
        self,
        payload: Mapping[str, Any],
        *,
        context: Mapping[str, Any] | None = None,
    ) -> GuardDecision:
        del context  # unused
        sanitized = _sanitize(deepcopy(payload))
        return GuardDecision(payload=sanitized)


__all__ = ["PIIRedactorGuard"]
