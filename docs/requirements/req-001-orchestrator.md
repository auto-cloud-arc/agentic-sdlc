# REQ-001: ForgeOps Maintenance Orchestrator

## Goals
1. Ingest facility telemetry events via HTTP API.
2. Evaluate a simple safety rule (`temperature > threshold`).
3. Create maintenance work orders when rule is triggered.
4. Write append-only audit logs with correlation IDs.
5. Provide optional notification emission via a stub mechanism.

## Non-goals
- Integrating with production CMMS/ticketing systems.
- Running distributed processing or message brokers.
- Implementing advanced rule authoring UI.
- Automating approval/merge decisions.

## User stories
- As a reliability engineer, I can submit telemetry events and get deterministic rule outcomes.
- As a maintenance lead, I receive a generated work order when thermal risk exceeds threshold.
- As a compliance auditor, I can review immutable audit records for key actions.
- As a workshop participant, I can run tests locally and observe end-to-end behavior quickly.

## Acceptance criteria
1. `POST /events` accepts valid telemetry event payloads and returns accepted status.
2. If `value > threshold`, the system creates a work order with traceable `source_event_id`.
3. If rule does not trigger, no work order is created.
4. Audit log entries are written for event ingestion and work-order creation.
5. Invalid payloads are rejected with HTTP 422 validation errors.
6. Notification capability exists as a non-blocking stub in flow.

## Non-functional requirements
- **Readability**: compact codebase suitable for live workshop walkthrough.
- **Testability**: deterministic unit/integration tests for critical paths.
- **Observability**: structured audit fields with timestamps and correlation IDs.
- **Portability**: runs locally with no external infrastructure.
- **Safety**: PR templates and CI checks enforce human review and verification.

## Open questions
1. Should thresholds eventually come from per-asset configuration?
2. How should invalid events be retained for investigation?
3. What escalation policy should notification channels follow?
4. Should schema changes be additive-only or major-versioned by endpoint?
