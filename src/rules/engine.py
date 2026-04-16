from src.domain.models import RuleDecision, TelemetryEvent


class ThresholdRulesEngine:
    """Evaluates telemetry events against a simple threshold policy."""

    def evaluate(self, event: TelemetryEvent) -> RuleDecision:
        if event.metric_value < event.threshold:
            return RuleDecision(
                action_required=False,
                reason=(
                    f"{event.metric_name}={event.metric_value} is below threshold {event.threshold}"
                ),
                priority="none",
            )

        priority = "high" if event.severity == "critical" else "medium"
        return RuleDecision(
            action_required=True,
            reason=(
                f"{event.metric_name}={event.metric_value} exceeded threshold {event.threshold}"
            ),
            priority=priority,
        )
