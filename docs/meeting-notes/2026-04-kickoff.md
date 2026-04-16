# ForgeOps Kickoff Notes

Date: 2026-04-15  
Attendees: Priya (PO), Marco (site reliability), Leah (platform), Dan (maintenance lead), workshop facilitator

## Raw Notes

- Need something small for the demo but it should feel like a real plant operations flow, not a toy todo app.
- Telemetry comes from plant gateways, probably already normalized, but someone said older sites still send weird field names.
- We only need one endpoint for the workshop. Maybe `POST /events` is enough.
- Temperature is the easiest signal to explain live. Pressure or vibration can come later if there is time.
- If a compressor is running hot, we should create a maintenance work order quickly, maybe under 2 seconds end to end.
- SRE wants a correlation ID on every step because audit reviews were painful last quarter.
- No PII. No technician phone numbers. No operator names. Keep it sanitized.
- Audit log cannot be editable after the fact. For the workshop, append-only in memory is probably okay.
- Need a demo path where nothing triggers too, not every event should become a ticket.
- A dispatch notification would be nice, but we do not need to call a real service.
- There was debate about whether to support multiple sites now or just one demo site. I think we should keep `site_id` in the payload anyway.
- Someone asked if severity comes from upstream or is computed here. No answer yet.
- We should show how Copilot helps turn this into issues, not just code.
- Include standards docs because the team keeps saying "we should standardize" without writing anything down.
- Need PR template to force test evidence and acceptance-criteria mapping.
- Codeowners should route docs to facilitators and app code to platform/backend owners.
- Maybe use FastAPI because it is readable and live coding is faster.
- Keep persistence in memory. No database setup during the workshop.
- Need a sample ADR for event schema versioning because upstream contracts always drift.

## Constraints And Non-Functional Notes

- Demo must fit in 90 minutes.
- Local setup should be under 5 minutes on a clean laptop.
- Logs should be structured enough to explain without bringing in a full observability stack.
- CI must run formatting, linting, and tests.
- No auto-merge. Human review remains required.

## Open Questions

- Do we want to reject unknown metrics or store them without action?
- Should severity influence priority directly or only help with notifications?
- What is the retention story for audit entries outside this workshop demo?
- Will notification stubs live in the same service or be split later?