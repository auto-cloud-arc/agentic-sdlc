# Demo 01: Meeting Notes To Requirements

## Objective

Turn ambiguous kickoff notes into a requirement document and an ADR.

## Facilitator Steps

1. Open `docs/meeting-notes/2026-04-kickoff.md`.
2. Highlight a few ambiguous lines about thresholds, correlation IDs, and notification scope.
3. Paste the prompt below into Copilot Chat.

## Exact Prompt

```text
Read docs/meeting-notes/2026-04-kickoff.md and draft a workshop-sized requirements document for ForgeOps Maintenance Orchestrator.

Write the result into docs/requirements/req-001-orchestrator.md and include:
- goals
- non-goals
- user stories
- functional requirements
- acceptance criteria
- non-functional requirements
- constraints
- open questions

Keep the scope to a single POST /events API, threshold-based rule evaluation, in-memory persistence, audit logging, and an optional notification stub. Avoid inventing external integrations.
```

## Expected Output

- A requirement document with testable acceptance criteria.
- A clear split between workshop goals and out-of-scope production concerns.
- A short list of unresolved questions that can later become issues or ADRs.

## Follow-Up Prompt

```text
Using docs/meeting-notes/2026-04-kickoff.md and docs/requirements/req-001-orchestrator.md, draft docs/requirements/adr-001-event-model.md.

Capture the event payload fields, why correlation_id is optional on input, and why additive schema evolution is preferred for this workshop.
```