# Observability standards

- Every rules-engine decision must produce an audit log entry.
- Event records must carry `site_id` so dashboards can distinguish facilities.
- Structured logging and correlation IDs should be added when the demo evolves beyond in-memory storage.
- Alerting paths should reference a runbook or operator action when integrated with real tooling.
- Observability data must stay free of PII.
