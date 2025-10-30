from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.deps import FeedbackRepository, get_feedback_repository

router = APIRouter()


class FeedbackRequest(BaseModel):
    claim_id: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    notes: str | None = Field(default=None, max_length=2000)


@router.post("/feedback")
def feedback(
    request: FeedbackRequest,
    repository: FeedbackRepository = Depends(get_feedback_repository),
) -> Dict[str, Any]:
    item = {
        "claim_id": request.claim_id,
        "label": request.label,
        "notes": request.notes,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }
    repository.put(item)
    return {"ok": True}


__all__ = ["router", "FeedbackRequest"]
