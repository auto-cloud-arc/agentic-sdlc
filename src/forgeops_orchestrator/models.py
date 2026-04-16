from __future__ import annotations

from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, Field

MetricType = Literal["temperature", "pressure", "vibration"]
SeverityType = Literal["info", "warning", "critical"]


class TelemetryEventIn(BaseModel):
    event_id: str = Field(default_factory=lambda: f"evt-{uuid4().hex[:10]}")
    site_id: str = Field(min_length=3, max_length=32)
    asset_id: str = Field(min_length=3, max_length=64)
    metric: MetricType
    value: float = Field(ge=-1000, le=10000)
    severity: SeverityType
    timestamp: str = Field(min_length=10)
    correlation_id: str | None = Field(default=None, min_length=8, max_length=64)


class RuleDecision(BaseModel):
    triggered: bool
    rule_name: str
    reason: str
    threshold: float | None = None


class WorkOrder(BaseModel):
    work_order_id: str = Field(default_factory=lambda: f"wo-{uuid4().hex[:8]}")
    site_id: str
    asset_id: str
    summary: str
    priority: Literal["medium", "high"]
    source_event_id: str
    correlation_id: str
    status: Literal["open"] = "open"


class AuditEntry(BaseModel):
    audit_id: str = Field(default_factory=lambda: f"aud-{uuid4().hex[:8]}")
    correlation_id: str
    event_id: str
    action: str
    outcome: str
    details: dict[str, str | float | bool | None]


class NotificationRecord(BaseModel):
    notification_id: str = Field(default_factory=lambda: f"ntf-{uuid4().hex[:8]}")
    channel: str
    correlation_id: str
    message: str


class EventProcessingResult(BaseModel):
    event_id: str
    correlation_id: str
    decision: RuleDecision
    work_order: WorkOrder | None = None
    notification_emitted: bool
    audit_entries_written: int
