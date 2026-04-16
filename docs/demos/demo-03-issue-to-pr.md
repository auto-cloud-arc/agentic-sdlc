# Demo 03 - Issue to Pull Request

## Script
1. Pick one issue (e.g., ingestion endpoint).
2. Ask Copilot for a minimal implementation + tests.
3. Open PR and complete guardrail checklist.

## Paste-ready Copilot prompt
```text
Implement issue #1 in /src/main.py and /tests/test_events.py.
Acceptance criteria:
- POST /events accepts valid payloads
- invalid payloads return 422
- include deterministic tests
Keep changes minimal and readable.
```

## PR checklist
- Link issue
- Map each AC to code/test evidence
- Include risk notes and rollback plan
- Confirm human reviewer approval required
