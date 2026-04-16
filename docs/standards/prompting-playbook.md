# Copilot Prompting Playbook

## Recommended prompt pattern
1. State the objective and constraint.
2. Provide exact file paths.
3. Request tests and acceptance criteria mapping.
4. Ask for minimal, reviewable changes.

## Good prompt examples
- "Implement `POST /events` in `/src/main.py` with FastAPI validation and add tests in `/tests/test_events.py` for happy path + invalid payload + audit log checks. Keep in-memory storage only."
- "Using `/docs/requirements/req-001-orchestrator.md`, propose 6 GitHub Issues with acceptance criteria and rollout risks."

## Bad prompt examples
- "Make everything production ready."
- "Add AI magic for maintenance."
- "Do whatever you think is best."

## Safety guardrails
- Never auto-merge pull requests.
- Always run tests and inspect diffs before approval.
- Require human sign-off on acceptance criteria and risk notes.
