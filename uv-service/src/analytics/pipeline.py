"""Core pipeline orchestration."""

import asyncio
from typing import Any

import httpx
import structlog
from pydantic import BaseModel

logger = structlog.get_logger()


class PipelineEvent(BaseModel):
    event_type: str
    source: str
    payload: dict[str, Any]
    timestamp: str


class AnalyticsPipeline:
    """Processes analytics events from multiple sources."""

    def __init__(self, api_url: str):
        self.api_url = api_url
        self.client = httpx.AsyncClient(base_url=api_url)

    async def ingest(self, event: PipelineEvent) -> dict:
        logger.info("ingesting_event", event_type=event.event_type, source=event.source)
        response = await self.client.post("/events", json=event.dict())
        return response.json()

    async def close(self):
        await self.client.aclose()
