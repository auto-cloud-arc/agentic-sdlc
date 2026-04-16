# Sample GitHub Issues

## Issue 1

- Type: Feature
- Title: Add `POST /events` ingestion endpoint
- Description: Accept validated telemetry events and return a processing result with correlation ID.
- Acceptance Criteria: Valid payload returns `202`; invalid payload returns `422`; response includes correlation ID.
- Test Plan: API tests for valid and invalid payloads.
- Logging And Telemetry: Record correlation ID on all accepted requests.
- Rollout Risk: Low, because the endpoint is isolated and in-memory.

## Issue 2

- Type: Feature
- Title: Implement threshold-based rules engine
- Description: Trigger maintenance only when a temperature event exceeds the configured threshold.
- Acceptance Criteria: Threshold breach triggers; non-triggering events remain accepted and audited.
- Test Plan: Unit or API tests for triggering and no-action scenarios.
- Logging And Telemetry: Capture rule name and decision outcome in audit details.
- Rollout Risk: Medium, because threshold logic is business behavior.

## Issue 3

- Type: Feature
- Title: Create in-memory work order persistence
- Description: Store generated work orders with IDs, priority, and source event linkage.
- Acceptance Criteria: Triggered events create exactly one work order with expected fields.
- Test Plan: Happy-path test asserts work order count and payload.
- Logging And Telemetry: Include work order ID in audit entries.
- Rollout Risk: Low.

## Issue 4

- Type: Feature
- Title: Add append-only audit logging
- Description: Record event ingestion and decision outcomes in an append-only audit list.
- Acceptance Criteria: Accepted events always create an ingestion audit record and a decision audit record.
- Test Plan: Assert audit entry count and action names after requests.
- Logging And Telemetry: Standardize `action`, `outcome`, and `details` fields.
- Rollout Risk: Medium, because audit consistency affects trust in the demo.

## Issue 5

- Type: Feature
- Title: Add notification stub for triggered work orders
- Description: Record a dispatch notification without calling an external service.
- Acceptance Criteria: Triggered events create one notification stub record.
- Test Plan: Verify notification count after a triggered event.
- Logging And Telemetry: Carry correlation ID into the stub record.
- Rollout Risk: Low.

## Issue 6

- Type: Feature
- Title: Add reusable CI and contributor standards
- Description: Introduce formatting, linting, tests, and repository guidance for workshop participants.
- Acceptance Criteria: CI runs Ruff format check, Ruff lint, and pytest through a reusable workflow.
- Test Plan: Validate workflow definitions and local commands.
- Logging And Telemetry: None beyond CI output.
- Rollout Risk: Low.

## Issue 7

- Type: Tech debt
- Title: Tighten observability language and correlation guidance
- Description: Align docs and code around structured audit fields and correlation ID expectations.
- Acceptance Criteria: Standards docs explicitly define required audit fields and correlation behavior.
- Test Plan: Review docs and ensure response payload exposes correlation ID.
- Logging And Telemetry: Central focus of the issue.
- Rollout Risk: Low.

## Issue 8

- Type: ADR request
- Title: Revisit event-model extensibility for unknown metrics
- Description: Decide how the service should evolve if upstream producers send metrics outside the current enum.
- Acceptance Criteria: ADR follow-up captures tradeoffs and next-step recommendation.
- Test Plan: None for the initial ADR request.
- Logging And Telemetry: Consider whether rejected metrics should still surface in metrics or audit summaries.
- Rollout Risk: Medium, because contract changes can ripple outward.