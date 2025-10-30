from __future__ import annotations

import os
from functools import lru_cache
from typing import Any, Dict

import boto3
from openai import OpenAI

from agents.registry import AgentRegistry


DEFAULT_REGION = "us-east-2"


@lru_cache(maxsize=1)
def get_settings() -> Dict[str, Any]:
    return {
        "region": os.environ.get("AWS_REGION", DEFAULT_REGION),
        "feedback_table": os.environ.get("FEEDBACK_TABLE"),
    }


@lru_cache(maxsize=1)
def get_openai_client() -> OpenAI:
    return OpenAI()


@lru_cache(maxsize=1)
def get_agent_registry() -> AgentRegistry:
    return AgentRegistry()


class FeedbackRepository:
    def __init__(self, table_name: str | None, region: str) -> None:
        self.table_name = table_name
        self.region = region
        self._fallback: list[Dict[str, Any]] = []
        self._dynamo = None
        if table_name:
            self._dynamo = boto3.resource("dynamodb", region_name=region).Table(table_name)

    def put(self, item: Dict[str, Any]) -> None:
        if self._dynamo is not None:
            self._dynamo.put_item(Item=item)
        else:
            self._fallback.append(item)

    @property
    def fallback_items(self) -> list[Dict[str, Any]]:
        return list(self._fallback)


@lru_cache(maxsize=1)
def get_feedback_repository() -> FeedbackRepository:
    settings = get_settings()
    return FeedbackRepository(settings["feedback_table"], settings["region"])


__all__ = [
    "DEFAULT_REGION",
    "FeedbackRepository",
    "get_agent_registry",
    "get_feedback_repository",
    "get_openai_client",
    "get_settings",
]
