# Demo 02: Requirements To Issues

## Objective

Break the requirements into implementation-ready GitHub issues.

## Facilitator Steps

1. Open `docs/requirements/req-001-orchestrator.md`.
2. Show the issue forms in `.github/ISSUE_TEMPLATE/`.
3. Paste the prompt below into Copilot Chat.

## Exact Prompt

```text
Using docs/requirements/req-001-orchestrator.md, generate 8 GitHub issues for this repository.

The issue set must cover:
- ingestion endpoint
- rules engine
- work order persistence
- audit logging
- notification stub
- CI and standards
- observability improvements
- ADR follow-up

For each issue, provide:
- title
- issue type
- short description
- acceptance criteria
- test plan
- logging or telemetry expectations
- rollout or review risk notes

Keep the issues small enough for a workshop and consistent with the issue templates in .github/ISSUE_TEMPLATE.
```

## Expected Issue Breakdown

- 5 feature issues for application behavior.
- 1 quality issue for CI and repo standards.
- 1 tech-debt issue for structured observability polish.
- 1 ADR issue to revisit event-model evolution decisions.

## Demo Tip

Compare the generated output against `docs/issues/sample-issues.md` to show what “good enough to implement” looks like.