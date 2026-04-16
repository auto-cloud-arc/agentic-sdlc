# Prompting Playbook

## Recommended Prompt Shape

- Name the file or folder you want Copilot to work in.
- State the objective in one sentence.
- Include concrete constraints such as tech stack, style rules, and acceptance criteria.
- Tell Copilot what not to do when that matters.

## Good Prompt Examples

- "In `src/forgeops_orchestrator/services.py`, add a pure helper that decides whether a temperature event should trigger maintenance. Keep it side-effect free and cover the threshold boundary in tests."
- "From `docs/meeting-notes/2026-04-kickoff.md`, draft a requirement spec with goals, non-goals, user stories, acceptance criteria, NFRs, and open questions. Keep it workshop-sized and avoid adding external integrations."
- "Create a pull request summary that maps each code change back to the acceptance criteria in `docs/requirements/req-001-orchestrator.md`."

## Weak Prompt Examples

- "Build the whole app for me."
- "Make this production ready."
- "Fix everything in the repo."

## Safety And Guardrails

- Never auto-merge AI-authored changes.
- Always run formatting, linting, and tests before requesting review.
- Require a human to confirm architecture changes, security-sensitive edits, and requirement interpretation.
- Ask Copilot to explain tradeoffs when the repo contains ambiguous requirements.