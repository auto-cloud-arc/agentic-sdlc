# Observability Standards

## Logging and audit
- Use structured fields, not free-form messages, for audit events.
- Include UTC timestamp for every audit record.
- Include `correlation_id` in all downstream records.

## Required audit fields
- `timestamp`
- `action`
- `correlation_id`
- `payload`

## Event flow checkpoints
1. Event accepted
2. Work order decision made
3. Work order created (when triggered)
4. Notification stub emitted (optional path)
