from datetime import datetime, timezone

from src.domain.models import NotificationRecord, TelemetryEvent


class NotificationService:
    def send(self, event: TelemetryEvent) -> NotificationRecord:
        message = (
            f"Maintenance action triggered for {event.asset_id} at {event.site_id}: "
            f"{event.metric_name}={event.metric_value}"
        )
        return NotificationRecord(
            site_id=event.site_id,
            channel="webhook",
            message=message,
            sent_at=datetime.now(timezone.utc),
        )
