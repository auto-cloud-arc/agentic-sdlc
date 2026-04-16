from __future__ import annotations

from datetime import datetime
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator

PROHIBITED_METADATA_KEYS = {"email", "phone", "ssn", "first_name", "last_name"}


class TelemetryEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    site_id: str
    asset_id: str
    metric_name: str
    metric_value: float
    threshold: float
    severity: Literal["info", "warning", "critical"]
    observed_at: datetime
    metadata: dict[str, str] = Field(default_factory=dict)

    @field_validator("metadata")
    @classmethod
    def reject_pii_metadata(cls, value: dict[str, str]) -> dict[str, str]:
        invalid_keys = {key for key in value if key.lower() in PROHIBITED_METADATA_KEYS}
        if invalid_keys:
            keys = ", ".join(sorted(invalid_keys))
            raise ValueError(f"PII is not allowed in telemetry metadata: {keys}")
        return value


class RuleDecision(BaseModel):
    action_required: bool
    reason: str
    priority: Literal["none", "medium", "high"]


class WorkOrder(BaseModel):
    work_order_id: str = Field(default_factory=lambda: f"wo-{uuid4().hex[:8]}")
    site_id: str
    asset_id: str
    summary: str
    priority: Literal["medium", "high"]
    created_at: datetime


class AuditLogEntry(BaseModel):
    audit_log_id: str = Field(default_factory=lambda: f"audit-{uuid4().hex[:8]}")
    site_id: str
    asset_id: str
    decision_reason: str
    action_required: bool
    recorded_at: datetime


class NotificationRecord(BaseModel):
    notification_id: str = Field(default_factory=lambda: f"notify-{uuid4().hex[:8]}")
    site_id: str
    channel: Literal["email", "webhook"]
    message: str
    sent_at: datetime


class ProcessingResult(BaseModel):
    decision: RuleDecision
    work_order: WorkOrder | None = None
    audit_log: AuditLogEntry
    notification: NotificationRecord | None = None
