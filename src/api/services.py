from datetime import datetime, timezone

from src.domain.models import AuditLogEntry, ProcessingResult, TelemetryEvent, WorkOrder
from src.notifications.service import NotificationService
from src.rules.engine import ThresholdRulesEngine
from src.storage.repository import InMemoryRepository


class MaintenanceOrchestrator:
    def __init__(
        self,
        repository: InMemoryRepository,
        rules_engine: ThresholdRulesEngine,
        notification_service: NotificationService,
    ) -> None:
        self.repository = repository
        self.rules_engine = rules_engine
        self.notification_service = notification_service

    def process_event(self, event: TelemetryEvent) -> ProcessingResult:
        decision = self.rules_engine.evaluate(event)
        work_order = None
        notification = None
        now = datetime.now(timezone.utc)

        if decision.action_required:
            work_order = self.repository.create_work_order(
                WorkOrder(
                    site_id=event.site_id,
                    asset_id=event.asset_id,
                    summary=f"Inspect {event.asset_id} for {event.metric_name} threshold breach",
                    priority=decision.priority,
                    created_at=now,
                )
            )
            notification = self.repository.record_notification(
                self.notification_service.send(event)
            )

        audit_log = self.repository.record_audit_entry(
            AuditLogEntry(
                site_id=event.site_id,
                asset_id=event.asset_id,
                decision_reason=decision.reason,
                action_required=decision.action_required,
                recorded_at=now,
            )
        )

        return ProcessingResult(
            decision=decision,
            work_order=work_order,
            audit_log=audit_log,
            notification=notification,
        )
