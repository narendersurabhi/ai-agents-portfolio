from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes import explain, feedback, rag, score
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
app.include_router(rag.router)

_WEB_ROOT = Path(__file__).resolve().parent.parent / "web"
if _WEB_ROOT.exists():
    app.mount("/static", StaticFiles(directory=_WEB_ROOT), name="frontend-static")

    @app.get("/", include_in_schema=False)
    async def serve_frontend() -> FileResponse:  # pragma: no cover - static file serving
        return FileResponse(_WEB_ROOT / "index.html")


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


__all__ = ["app"]
