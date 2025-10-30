from __future__ import annotations

import json
import os
from functools import lru_cache
from typing import Any, Dict

import boto3
from openai import OpenAI

from agents.guards import GuardChain
from agents.guards.pii_redactor import PIIRedactorGuard
from agents.guards.prompt_injection import PromptInjectionGuard
from agents.guards.relevance import RelevanceGuard
from agents.manager import ManagerAgent, ManagerConfig
from agents.registry import AgentRegistry


DEFAULT_REGION = "us-east-2"
DEFAULT_HITL_THRESHOLD = 0.85


@lru_cache(maxsize=1)
def get_settings() -> Dict[str, Any]:
    return {
        "region": os.environ.get("AWS_REGION", DEFAULT_REGION),
        "feedback_table": os.environ.get("FEEDBACK_TABLE"),
        "hitl_threshold": float(os.environ.get("HITL_RISK_THRESHOLD", DEFAULT_HITL_THRESHOLD)),
        "sns_handoff_topic": os.environ.get("SNS_HANDOFF_TOPIC_ARN"),
    }


@lru_cache(maxsize=1)
def get_openai_client() -> OpenAI:
    return OpenAI()


@lru_cache(maxsize=1)
def get_agent_registry() -> AgentRegistry:
    return AgentRegistry()


@lru_cache(maxsize=1)
def get_guard_chain() -> GuardChain:
    return GuardChain(
        [
            PIIRedactorGuard(),
            PromptInjectionGuard(),
            RelevanceGuard(),
        ]
    )


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


class HandoffPublisher:
    def __init__(self, topic_arn: str | None, region: str) -> None:
        self.topic_arn = topic_arn
        self.region = region
        self._sns = None
        if topic_arn:
            self._sns = boto3.client("sns", region_name=region)

    def publish(self, payload: Dict[str, Any]) -> None:
        if not self.topic_arn or self._sns is None:
            return
        self._sns.publish(
            TopicArn=self.topic_arn,
            Message=json.dumps(payload, sort_keys=True),
        )


@lru_cache(maxsize=1)
def get_feedback_repository() -> FeedbackRepository:
    settings = get_settings()
    return FeedbackRepository(settings["feedback_table"], settings["region"])


@lru_cache(maxsize=1)
def get_handoff_publisher() -> HandoffPublisher:
    settings = get_settings()
    return HandoffPublisher(settings["sns_handoff_topic"], settings["region"])


@lru_cache(maxsize=1)
def get_manager_agent() -> ManagerAgent:
    registry = get_agent_registry()
    client = get_openai_client()
    settings = get_settings()
    config = ManagerConfig(hitl_threshold=settings["hitl_threshold"])
    return ManagerAgent(registry, client, config)


__all__ = [
    "DEFAULT_REGION",
    "DEFAULT_HITL_THRESHOLD",
    "FeedbackRepository",
    "HandoffPublisher",
    "get_agent_registry",
    "get_feedback_repository",
    "get_guard_chain",
    "get_handoff_publisher",
    "get_manager_agent",
    "get_openai_client",
    "get_settings",
]
