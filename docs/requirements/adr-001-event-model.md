# ADR-001 Event Model And Versioning

- Status: Accepted
- Date: 2026-04-15

## Context

The workshop needs an event contract that is easy to explain live, strict enough to validate, and realistic enough to motivate an ADR. The upstream telemetry ecosystem is expected to evolve over time, especially as more sites and signal types are added.

## Decision

- Use a single JSON event payload for `POST /events` with these fields:
  - `event_id`
  - `site_id`
  - `asset_id`
  - `metric`
  - `value`
  - `severity`
  - `timestamp`
  - `correlation_id` optional
- Constrain `metric` to a known set for the demo: `temperature`, `pressure`, `vibration`.
- Keep `correlation_id` optional on input and generate one when absent.
- Version by additive evolution rather than multiple endpoint versions for the workshop.

## Rationale

- A narrow schema keeps validation and testing small.
- Enumerated metrics make invalid input behavior obvious in the demo.
- Generating a correlation ID in the service supports observability discussion without requiring all producers to be updated first.
- Additive schema evolution is easier to explain than URL-based versioning in a short workshop.

## Consequences

- Breaking field renames should require a new ADR or explicit versioning strategy.
- Unknown metrics are rejected today, which is simple but may be too rigid for real integrations.
- The event model favors clarity over extensibility; future workshop iterations can add envelope metadata if needed.