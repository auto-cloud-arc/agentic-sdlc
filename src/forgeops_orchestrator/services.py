from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4

from .models import (
    AuditEntry,
    EventProcessingResult,
    NotificationRecord,
    RuleDecision,
    TelemetryEventIn,
    WorkOrder,
)

TEMPERATURE_THRESHOLD = 90.0


@dataclass
class InMemoryStore:
    events: list[TelemetryEventIn] = field(default_factory=list)
    work_orders: list[WorkOrder] = field(default_factory=list)
    audit_entries: list[AuditEntry] = field(default_factory=list)
    notifications: list[NotificationRecord] = field(default_factory=list)

    def reset(self) -> None:
        self.events.clear()
        self.work_orders.clear()
        self.audit_entries.clear()
        self.notifications.clear()


def ensure_correlation_id(candidate: str | None) -> str:
    return candidate or f"corr-{uuid4().hex[:10]}"


def evaluate_rules(event: TelemetryEventIn) -> RuleDecision:
    if event.metric == "temperature" and event.value > TEMPERATURE_THRESHOLD:
        return RuleDecision(
            triggered=True,
            rule_name="temperature_above_threshold",
            reason=f"Temperature {event.value} exceeded threshold {TEMPERATURE_THRESHOLD}",
            threshold=TEMPERATURE_THRESHOLD,
        )

    return RuleDecision(
        triggered=False,
        rule_name="no_action",
        reason="Event recorded without maintenance trigger",
    )


def append_audit_entry(
    store: InMemoryStore,
    *,
    correlation_id: str,
    event_id: str,
    action: str,
    outcome: str,
    details: dict[str, str | float | bool | None],
) -> None:
    store.audit_entries.append(
        AuditEntry(
            correlation_id=correlation_id,
            event_id=event_id,
            action=action,
            outcome=outcome,
            details=details,
        )
    )


def build_work_order(event: TelemetryEventIn, correlation_id: str) -> WorkOrder:
    return WorkOrder(
        site_id=event.site_id,
        asset_id=event.asset_id,
        summary=(
            f"Inspect {event.asset_id} at {event.site_id} for elevated {event.metric} reading"
        ),
        priority="high" if event.severity == "critical" else "medium",
        source_event_id=event.event_id,
        correlation_id=correlation_id,
    )


def emit_notification_stub(
    store: InMemoryStore, correlation_id: str, work_order: WorkOrder
) -> NotificationRecord:
    notification = NotificationRecord(
        channel="maintenance-dispatch",
        correlation_id=correlation_id,
        message=f"Dispatch requested for {work_order.work_order_id} ({work_order.asset_id})",
    )
    store.notifications.append(notification)
    return notification


def process_event(event: TelemetryEventIn, store: InMemoryStore) -> EventProcessingResult:
    correlation_id = ensure_correlation_id(event.correlation_id)
    normalized_event = event.model_copy(update={"correlation_id": correlation_id})
    store.events.append(normalized_event)

    append_audit_entry(
        store,
        correlation_id=correlation_id,
        event_id=normalized_event.event_id,
        action="event_ingested",
        outcome="accepted",
        details={"metric": normalized_event.metric, "value": normalized_event.value},
    )

    decision = evaluate_rules(normalized_event)
    work_order = None
    notification_emitted = False

    if decision.triggered:
        work_order = build_work_order(normalized_event, correlation_id)
        store.work_orders.append(work_order)
        emit_notification_stub(store, correlation_id, work_order)
        notification_emitted = True
        append_audit_entry(
            store,
            correlation_id=correlation_id,
            event_id=normalized_event.event_id,
            action="work_order_created",
            outcome="triggered",
            details={
                "rule_name": decision.rule_name,
                "work_order_id": work_order.work_order_id,
                "priority": work_order.priority,
            },
        )
    else:
        append_audit_entry(
            store,
            correlation_id=correlation_id,
            event_id=normalized_event.event_id,
            action="rule_evaluated",
            outcome="no_action",
            details={"rule_name": decision.rule_name, "triggered": False},
        )

    return EventProcessingResult(
        event_id=normalized_event.event_id,
        correlation_id=correlation_id,
        decision=decision,
        work_order=work_order,
        notification_emitted=notification_emitted,
        audit_entries_written=sum(
            1 for entry in store.audit_entries if entry.event_id == event.event_id
        ),
    )
