from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="ForgeOps Maintenance Orchestrator", version="0.1.0")


events_store: list[dict] = []
work_orders_store: list[dict] = []
audit_log_store: list[dict] = []


class TelemetryEvent(BaseModel):
    event_id: str
    facility_id: str
    asset_id: str
    event_type: Literal["telemetry.temperature"]
    metric: Literal["temperature"]
    value: float
    threshold: float = Field(gt=-1000, lt=5000)
    timestamp: datetime
    correlation_id: str | None = None


class EventResponse(BaseModel):
    status: Literal["accepted"]
    work_order_created: bool
    work_order_id: str | None = None


def append_audit(action: str, correlation_id: str, payload: dict) -> None:
    audit_log_store.append(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "correlation_id": correlation_id,
            "payload": payload,
        }
    )


def should_create_work_order(event: TelemetryEvent) -> bool:
    return event.value > event.threshold


def emit_notification_stub(work_order: dict) -> None:
    append_audit(
        action="notification_stub_emitted",
        correlation_id=work_order["correlation_id"],
        payload={"work_order_id": work_order["work_order_id"]},
    )


@app.post("/events", response_model=EventResponse)
def ingest_event(event: TelemetryEvent) -> EventResponse:
    correlation_id = event.correlation_id or event.event_id
    event_record = event.model_dump(mode="json")
    event_record["correlation_id"] = correlation_id
    events_store.append(event_record)
    append_audit("event_ingested", correlation_id, {"event_id": event.event_id})

    if not should_create_work_order(event):
        return EventResponse(status="accepted", work_order_created=False)

    work_order_id = f"WO-{uuid4().hex[:8].upper()}"
    work_order = {
        "work_order_id": work_order_id,
        "facility_id": event.facility_id,
        "asset_id": event.asset_id,
        "reason": (f"Temperature {event.value} exceeded threshold {event.threshold}"),
        "source_event_id": event.event_id,
        "correlation_id": correlation_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    work_orders_store.append(work_order)
    append_audit("work_order_created", correlation_id, {"work_order_id": work_order_id})
    emit_notification_stub(work_order)

    return EventResponse(
        status="accepted",
        work_order_created=True,
        work_order_id=work_order_id,
    )


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/audit-logs")
def audit_logs() -> dict:
    return {"items": audit_log_store}


@app.post("/reset")
def reset_state() -> dict:
    events_store.clear()
    work_orders_store.clear()
    audit_log_store.clear()
    return {"status": "reset"}
