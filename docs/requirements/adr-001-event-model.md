# ADR-001: Event model and versioning approach

- **Status:** Proposed
- **Date:** 2026-04-16

## Context

ForgeOps needs a telemetry event shape that is easy to demo, easy to validate, and safe to share. The model must support multiple sites, threshold evaluation, and auditability without introducing PII.

## Decision

Use a compact event contract with these required fields:

- `site_id`
- `asset_id`
- `metric_name`
- `metric_value`
- `threshold`
- `severity`
- `observed_at`
- `metadata`

The demo keeps versioning lightweight by treating `REQ-001` as the contract baseline and rejecting unexpected fields in the API model. Downstream services can add an explicit schema version once the contract stabilizes across teams.

## Consequences

- The event contract stays small enough for live demos and code reviews.
- Rejecting extra fields reduces accidental drift and discourages hidden PII.
- Future schema evolution will likely require a version field and migration strategy.
