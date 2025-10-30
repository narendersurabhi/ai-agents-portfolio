from __future__ import annotations

import json
import logging
import threading
from collections import defaultdict, deque
from dataclasses import dataclass
from time import perf_counter
from typing import Any, Deque, Dict, Mapping

DEFAULT_LOGGER_NAME = "agentic"
MAX_METRIC_SAMPLES = 100

MODEL_PRICING: Dict[str, Dict[str, float]] = {
    "gpt-5": {"input": 0.010, "output": 0.030},
}


class JsonFormatter(logging.Formatter):
    """Simple JSON log formatter for structured logging."""

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        payload = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "event": getattr(record, "event", record.getMessage()),
            "time": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
        }
        extra_fields = getattr(record, "fields", None)
        if isinstance(extra_fields, Mapping):
            payload.update(extra_fields)
        return json.dumps(payload, sort_keys=True)


_logger_lock = threading.Lock()
_logger: logging.Logger | None = None


def configure_logging(level: int = logging.INFO) -> logging.Logger:
    global _logger
    with _logger_lock:
        if _logger is None:
            handler = logging.StreamHandler()
            handler.setFormatter(JsonFormatter())
            logging.basicConfig(level=level, handlers=[handler], force=True)
            _logger = logging.getLogger(DEFAULT_LOGGER_NAME)
            _logger.setLevel(level)
        return _logger


@dataclass
class TokenStats:
    model: str
    calls: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    total_cost_usd: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self.model,
            "calls": self.calls,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
            "total_cost_usd": round(self.total_cost_usd, 6),
        }


class Metrics:
    def __init__(self, sample_size: int = MAX_METRIC_SAMPLES) -> None:
        self._latency: Dict[str, Deque[float]] = defaultdict(lambda: deque(maxlen=sample_size))
        self._tokens: Dict[str, TokenStats] = {}
        self._lock = threading.Lock()

    def record_latency(self, route: str, duration_ms: float) -> None:
        with self._lock:
            self._latency[route].append(duration_ms)

    def route_p95(self, route: str) -> float:
        with self._lock:
            samples = list(self._latency.get(route, ()))
        if not samples:
            return 0.0
        if len(samples) == 1:
            return float(samples[0])
        samples.sort()
        index = max(int(0.95 * (len(samples) - 1)), 0)
        return float(samples[index])

    def record_tokens(
        self,
        agent: str,
        model: str,
        *,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
        total_tokens: int | None = None,
    ) -> Dict[str, Any]:
        prompt_tokens = int(prompt_tokens or 0)
        completion_tokens = int(completion_tokens or 0)
        computed_total = prompt_tokens + completion_tokens
        total_tokens = int(total_tokens if total_tokens is not None else computed_total)

        pricing = MODEL_PRICING.get(model, {"input": 0.0, "output": 0.0})
        cost = (prompt_tokens / 1000) * pricing.get("input", 0.0)
        cost += (completion_tokens / 1000) * pricing.get("output", 0.0)

        with self._lock:
            stats = self._tokens.setdefault(agent, TokenStats(model=model))
            stats.calls += 1
            stats.prompt_tokens += prompt_tokens
            stats.completion_tokens += completion_tokens
            stats.total_tokens += total_tokens
            stats.total_cost_usd += cost
            snapshot = stats.to_dict()
        snapshot["last_call_cost_usd"] = round(cost, 6)
        return snapshot

    def snapshot(self) -> Dict[str, Any]:
        with self._lock:
            latency = {route: list(values) for route, values in self._latency.items()}
            tokens = {agent: stats.to_dict() for agent, stats in self._tokens.items()}
        return {"latency_samples_ms": latency, "token_usage": tokens}

    def reset(self) -> None:
        with self._lock:
            self._latency.clear()
            self._tokens.clear()


_metrics = Metrics()


def get_metrics() -> Metrics:
    return _metrics


def log_event(event: str, **fields: Any) -> None:
    logger = _logger or configure_logging()
    logger.info(event, extra={"event": event, "fields": fields})


class Timer:
    def __init__(self) -> None:
        self._start = perf_counter()

    def stop(self) -> float:
        end = perf_counter()
        duration = (end - self._start) * 1000
        self._start = end
        return duration


__all__ = [
    "MODEL_PRICING",
    "Metrics",
    "Timer",
    "configure_logging",
    "get_metrics",
    "log_event",
]
