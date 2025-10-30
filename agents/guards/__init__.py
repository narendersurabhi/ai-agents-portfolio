from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, MutableMapping, Protocol, Sequence


class Guard(Protocol):
    name: str

    def run(
        self,
        payload: Mapping[str, Any],
        *,
        context: Mapping[str, Any] | None = None,
    ) -> "GuardDecision":
        ...


@dataclass(frozen=True)
class GuardDecision:
    """Result returned by individual guards."""

    payload: Mapping[str, Any] | None = None
    handoff: bool = False
    reason: str | None = None


@dataclass(frozen=True)
class GuardOutcome:
    """Aggregated decision after applying all guards."""

    payload: Mapping[str, Any]
    handoff: bool
    guard: str | None = None
    reason: str | None = None


class GuardChain:
    """Applies a sequence of guards to a payload."""

    def __init__(self, guards: Sequence[Guard]) -> None:
        self._guards = list(guards)

    def run(
        self,
        payload: Mapping[str, Any],
        *,
        context: Mapping[str, Any] | None = None,
    ) -> GuardOutcome:
        current: MutableMapping[str, Any] | Mapping[str, Any] = payload
        ctx = context or {}
        for guard in self._guards:
            decision = guard.run(current, context=ctx)
            if decision.payload is not None:
                current = decision.payload
            if decision.handoff:
                return GuardOutcome(
                    payload=current,
                    handoff=True,
                    guard=guard.name,
                    reason=decision.reason,
                )
        if not isinstance(current, Mapping):
            raise TypeError("Guard chain payload must remain a mapping")
        return GuardOutcome(payload=current, handoff=False)


__all__ = ["Guard", "GuardChain", "GuardDecision", "GuardOutcome"]
