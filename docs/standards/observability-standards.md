# Observability Standards

## Logging Principles

- Prefer structured fields over prose-heavy log lines.
- Carry a `correlation_id` across request handling, rule evaluation, audit logging, and notifications.
- Avoid sensitive identifiers that are not needed for troubleshooting.

## Audit Log Fields

- `audit_id`
- `correlation_id`
- `event_id`
- `action`
- `outcome`
- `details`

## Decision Trace Expectations

- Record one audit entry when an event is accepted.
- Record one audit entry when the rule evaluation completes.
- Record one audit entry when a work order is created.
- Keep audit logs append-only. Corrections should be represented by new entries, not mutation.

## Workshop Note

The demo stores audit records in memory, but the field design should still reflect what a real compliance or incident-review flow would need.