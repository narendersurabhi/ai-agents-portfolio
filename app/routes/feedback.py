from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.deps import (
    FeedbackRepository,
    HandoffPublisher,
    get_feedback_repository,
    get_handoff_publisher,
)

router = APIRouter()


class FeedbackRequest(BaseModel):
    claim_id: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    notes: str | None = Field(default=None, max_length=2000)
    handoff: bool | None = Field(default=False)


@router.post("/feedback")
def feedback(
    request: FeedbackRequest,
    repository: FeedbackRepository = Depends(get_feedback_repository),
    publisher: HandoffPublisher = Depends(get_handoff_publisher),
) -> Dict[str, Any]:
    item = {
        "claim_id": request.claim_id,
        "label": request.label,
        "notes": request.notes,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }
    repository.put(item)
    if request.handoff:
        publisher.publish(
            {
                "flow": "feedback",
                "claim_id": request.claim_id,
                "label": request.label,
                "notes": request.notes,
            }
        )
    return {"ok": True}


__all__ = ["router", "FeedbackRequest"]
