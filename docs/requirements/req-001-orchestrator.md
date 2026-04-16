# Requirement REQ-001: ForgeOps Maintenance Orchestrator

## Problem statement

Design intent is getting lost between kickoff meetings, backlog refinement, and implementation. ForgeOps needs a repeatable way to turn telemetry-driven maintenance ideas into clear engineering requirements, actionable issues, and guarded pull requests.

## Goals

- Convert telemetry events into actionable maintenance work orders.
- Generate notifications for actionable maintenance conditions.
- Record an audit trail for every evaluation decision.
- Provide a compact demo repository that shows how standards and guardrails travel with the work.

## Non-goals

- Real integration with CMMS, email, or paging tools.
- Long-term persistence beyond an in-memory demo implementation.
- Tenant-specific authorization or identity management.

## User stories

- As a Product Owner, I want actionable events to become work orders so that site teams can triage faster.
- As an SRE, I want every decision recorded so that incident reviews can explain why work was or was not created.
- As a Platform Engineer, I want standards and workflows codified so that teams can reuse them with minimal setup.

## Functional requirements

1. The service shall expose `POST /events` for telemetry ingestion.
2. The service shall evaluate incoming events against threshold-based rules.
3. The service shall create a work order when an event exceeds its configured threshold.
4. The service shall record an audit log entry for every evaluation.
5. The service shall emit a notification stub for actionable events.
6. The repository shall include issue, PR, and workflow templates that encode the demo guardrails.

## Non-functional requirements

- Actionable event processing should complete within 2 seconds in the demo path.
- Event payloads, logs, and fixtures must not contain PII.
- The workflow must support multiple sites through explicit `site_id` fields.
- New behavior must be covered by tests and validated in CI.

## Constraints

- Use a compact Python + FastAPI stack for workshop readability.
- Keep dependencies minimal and broadly understandable.
- Prefer reusable GitHub configuration over tool-specific tribal knowledge.

## Assumptions

- Thresholds are supplied with each event for demo simplicity.
- In-memory persistence is acceptable for the workshop narrative.
- A webhook-style notification stub is sufficient for the first walkthrough.

## Open questions

- Should the first production-grade version support both webhooks and email notifications?
- What audit-log retention policy should downstream implementations adopt?
- Which teams should own shared workflows once multiple services adopt them?

## Acceptance criteria

- [ ] `POST /events` accepts a valid multi-site telemetry event and returns a decision summary.
- [ ] Threshold breaches create a work order, an audit entry, and a notification record.
- [ ] Non-actionable events still create an audit entry but do not create work orders.
- [ ] Payloads that contain prohibited PII-style metadata are rejected.
- [ ] Repository standards, templates, and workflows are documented and discoverable.
- [ ] Local and CI validation run linting and tests.
