from src.domain.models import AuditLogEntry, NotificationRecord, WorkOrder


class InMemoryRepository:
    def __init__(self) -> None:
        self.work_orders: list[WorkOrder] = []
        self.audit_log: list[AuditLogEntry] = []
        self.notifications: list[NotificationRecord] = []

    def create_work_order(self, work_order: WorkOrder) -> WorkOrder:
        self.work_orders.append(work_order)
        return work_order

    def record_audit_entry(self, entry: AuditLogEntry) -> AuditLogEntry:
        self.audit_log.append(entry)
        return entry

    def record_notification(self, notification: NotificationRecord) -> NotificationRecord:
        self.notifications.append(notification)
        return notification
