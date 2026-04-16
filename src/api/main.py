from fastapi import FastAPI, status

from src.api.services import MaintenanceOrchestrator
from src.domain.models import AuditLogEntry, ProcessingResult, TelemetryEvent, WorkOrder
from src.notifications.service import NotificationService
from src.rules.engine import ThresholdRulesEngine
from src.storage.repository import InMemoryRepository


def create_app() -> FastAPI:
    repository = InMemoryRepository()
    orchestrator = MaintenanceOrchestrator(
        repository=repository,
        rules_engine=ThresholdRulesEngine(),
        notification_service=NotificationService(),
    )

    app = FastAPI(title="ForgeOps Maintenance Orchestrator", version="0.1.0")
    app.state.repository = repository
    app.state.orchestrator = orchestrator

    @app.get("/health")
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/events", response_model=ProcessingResult, status_code=status.HTTP_202_ACCEPTED)
    def ingest_event(event: TelemetryEvent) -> ProcessingResult:
        return app.state.orchestrator.process_event(event)

    @app.get("/work-orders", response_model=list[WorkOrder])
    def list_work_orders() -> list[WorkOrder]:
        return app.state.repository.work_orders

    @app.get("/audit-log", response_model=list[AuditLogEntry])
    def list_audit_log() -> list[AuditLogEntry]:
        return app.state.repository.audit_log

    return app


app = create_app()
