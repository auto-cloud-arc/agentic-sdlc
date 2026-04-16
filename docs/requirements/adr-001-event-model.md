# ADR-001: Telemetry Event Model and Versioning

## Status
Accepted

## Context
The workshop needs a stable event contract that is easy to reason about while still showing realistic lifecycle concerns. We need clear forward compatibility guidance without introducing heavy schema tooling.

## Decision
Use a single JSON event model for v1 ingestion with explicit semantic fields:
- `event_id`, `facility_id`, `asset_id`
- `event_type` fixed to `telemetry.temperature`
- `metric` fixed to `temperature`
- `value`, `threshold`, `timestamp`
- optional `correlation_id`

Versioning strategy:
1. Keep endpoint at `POST /events` for workshop simplicity.
2. Prefer additive, backward-compatible fields within v1.
3. Introduce breaking changes only via a new endpoint version (e.g., `/v2/events`).
4. Keep rule logic deterministic and explicit to preserve test stability.

## Consequences
### Positive
- Small and teachable schema for workshop participants.
- Easy validation with FastAPI/Pydantic.
- Encourages compatibility discipline early.

### Negative
- Limited flexibility for mixed metric types in v1.
- No schema registry integration in this demo.

## Alternatives considered
- Multi-metric polymorphic event schema in v1 (rejected: too complex for 90-minute workshop).
- Version embedded in payload only (rejected: less explicit migration path for breaking changes).
