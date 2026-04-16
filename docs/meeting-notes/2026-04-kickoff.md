# Kickoff Notes - April 2026

Attendees: Ops manager, maintenance lead, reliability engineer, IT security, workshop facilitator

## Raw notes (intentionally messy)
- Need "something Copilot can help build fast" for thermal excursions in older facilities.
- Incoming telemetry from edge gateway every 15-30 sec, but workshop can fake with API calls.
- "If temp is above allowed threshold, create a work order immediately" (question: static threshold or per-asset config?)
- Compliance needs evidence trail; append-only log preferred.
- Maybe send notifications later; for demo maybe print or stub.
- Must show this is not autonomous release: human approval in PR is required.
- NFR: easy to explain in 90-minute session, should run on laptop.
- NFR: deterministic test data (no flaky examples).
- Constraint: no real CMMS integration in workshop.
- Constraint: avoid cloud dependencies for live demo.
- Security asked for correlation IDs in logs and audit entries.
- We should track false alarms somehow (not in v1?).
- Open question: what event schema versioning approach keeps backward compatibility clear?
- Open question: should invalid telemetry be stored for forensics, or rejected only?
