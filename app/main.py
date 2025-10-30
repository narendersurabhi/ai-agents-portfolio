from __future__ import annotations

from fastapi import FastAPI, Request

from app.routes import explain, feedback, score
from observability import Timer, configure_logging, get_metrics, log_event

configure_logging()
app = FastAPI(title="Agentic FWA API", version="0.1.0")
_metrics = get_metrics()


@app.middleware("http")
async def observability_middleware(request: Request, call_next):  # type: ignore[override]
    timer = Timer()
    path = request.url.path
    method = request.method
    try:
        response = await call_next(request)
    except Exception as exc:  # pragma: no cover - passthrough to FastAPI exception handlers
        duration_ms = timer.stop()
        _metrics.record_latency(path, duration_ms)
        log_event(
            "http.request.error",
            path=path,
            method=method,
            status=500,
            duration_ms=round(duration_ms, 2),
            p95_ms=round(_metrics.route_p95(path), 2),
            error=type(exc).__name__,
        )
        raise
    else:
        duration_ms = timer.stop()
        _metrics.record_latency(path, duration_ms)
        log_event(
            "http.request.complete",
            path=path,
            method=method,
            status=response.status_code,
            duration_ms=round(duration_ms, 2),
            p95_ms=round(_metrics.route_p95(path), 2),
        )
        return response


app.include_router(score.router)
app.include_router(explain.router)
app.include_router(feedback.router)


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


__all__ = ["app"]
