# REQ-001 ForgeOps Maintenance Orchestrator

## Goals

- Ingest facility telemetry events through a single HTTP endpoint.
- Evaluate a simple rule set suitable for live explanation in a workshop.
- Create maintenance work orders when a threshold-based rule triggers.
- Persist events, work orders, notifications, and audit records in memory for the demo.
- Demonstrate a clean path from meeting notes to issues, code, tests, and pull request controls.

## Non-Goals

- Integrate with a real CMMS, paging platform, historian, or message broker.
- Support full multi-tenant authorization or operator identity management.
- Model every telemetry type or advanced predictive maintenance behavior.
- Provide production-ready persistence or retention management.

## Users And User Stories

- As a maintenance coordinator, I want a high-temperature event to create a work order so that I can dispatch technicians quickly.
- As an SRE, I want correlation IDs and append-only audit records so that I can explain the service decision path during incident review.
- As a platform engineer, I want templates and standards in the repository so that Copilot-assisted changes stay reviewable and consistent.
- As a workshop participant, I want the code and docs to stay small enough to understand in one session.

## Functional Requirements

### Event Ingestion

- The system shall expose `POST /events`.
- The API shall accept an event with `event_id`, `site_id`, `asset_id`, `metric`, `value`, `severity`, `timestamp`, and optional `correlation_id`.
- The API shall reject invalid payloads with a validation error.

### Rule Evaluation

- The system shall evaluate a temperature threshold rule.
- A temperature event with `value > 90.0` shall trigger maintenance action.
- Events that do not match the rule shall still be stored and audited.

### Work Orders And Notifications

- Triggered events shall create a work order with a generated work order ID.
- Work order priority shall be `high` for `critical` events and `medium` for `warning` events.
- Triggered events shall append a notification stub record showing what dispatch message would have been sent.

### Auditability

- Every accepted event shall produce an ingestion audit record.
- Every rule outcome shall produce an audit record describing the decision.
- Audit records shall include `correlation_id`, `event_id`, `action`, `outcome`, and decision details.

## Acceptance Criteria

1. A valid critical temperature event above threshold returns `202` and includes a created work order in the response.
2. An invalid event payload returns `422` and does not create a work order or audit record.
3. A non-triggering event returns `202`, is stored, and writes audit records showing acceptance and no-action evaluation.
4. Every accepted event has a correlation ID in the response, even when one is not provided by the caller.
5. The repository includes issue forms, a PR template, CODEOWNERS, and reusable CI that runs formatting, linting, and tests.

## Non-Functional Requirements

- Keep local setup under 5 minutes.
- Keep code and tests readable for a 90-minute live workshop.
- Keep the event-to-decision logic simple enough to explain in under 10 minutes.
- Avoid PII in payloads, logs, and examples.
- Prefer structured fields over free-form log strings where possible.

## Dependencies And Constraints

- In-memory persistence is acceptable for the workshop.
- The project shall use Python, FastAPI, pytest, and Ruff.
- No external services are required to run the demo locally.

## Open Questions

- Should future versions treat unknown metrics as validation errors or dead-letter candidates?
- Should severity be optional if the upstream producer cannot supply it?
- When the workshop grows beyond one service, should notifications move behind an interface boundary?