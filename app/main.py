from __future__ import annotations

from fastapi import FastAPI

from app.routes import explain, feedback, score

app = FastAPI(title="Agentic FWA API", version="0.1.0")

app.include_router(score.router)
app.include_router(explain.router)
app.include_router(feedback.router)


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


__all__ = ["app"]
