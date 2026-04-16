# Kickoff Notes - ForgeOps Maintenance Orchestrator

## Raw notes

- Need alerts for critical maintenance events before operators miss another threshold breach.
- Work orders must be generated from telemetry, not handwritten after the fact.
- Audit log is mandatory for every decision because the PO wants post-incident traceability.
- No PII in event payloads, logs, demos, or fixtures.
- Event-to-ticket latency target is under 2 seconds for actionable events.
- Must support multiple sites with shared standards and reusable workflows.
- Need something small enough to demo end to end in one session.
- SRE wants structured logs, correlation IDs, and a runbook link in alert paths.
- Platform team wants issue templates, PR templates, CODEOWNERS, and CI gates.
- Open question: do we notify by email, webhook, or both in the first release?
- Open question: how long do we retain audit logs in a real deployment?
