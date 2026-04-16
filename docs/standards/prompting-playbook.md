# Prompting playbook

## Good prompts

- "Turn `/docs/meeting-notes/2026-04-kickoff.md` into a requirement with goals, non-goals, acceptance criteria, and open questions."
- "Create a feature issue from `REQ-001` for `POST /events`, including scope, acceptance criteria, logging expectations, and a test plan."
- "Implement the ingestion issue in `src/api` and `tests`, then explain how the code maps back to the acceptance criteria."

## Weak prompts

- "Build the whole thing."
- "Fix everything in this repo."
- "Add whatever tests you think make sense."

## Team rules

- Anchor prompts to a source artifact such as a requirement or issue.
- State the boundaries of the change explicitly.
- Ask for tests and acceptance-criteria mapping, not just code.
- Require a human review before merge.
