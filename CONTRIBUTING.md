# Contributing

## Working agreement

This repository demonstrates an agentic SDLC workflow where AI assists with drafting and implementation, but humans remain accountable for scope, correctness, and rollout decisions.

## Definition of done

A change is done when all of the following are true:

- Requirements or acceptance criteria are updated when behavior changes.
- The PR description maps code changes back to acceptance criteria.
- New or changed behavior is covered by tests.
- Auditability and observability expectations are addressed.
- `ruff check .` passes.
- `python -m unittest discover -s tests -v` passes.
- Reviewer approval is captured before merge.

## Development workflow

1. Start from the relevant requirement, issue, or ADR.
2. Keep changes small enough to review safely.
3. Prefer explicit, testable acceptance criteria.
4. Avoid introducing PII into sample payloads, fixtures, or logs.
5. Use the templates in `.github/` for issues and pull requests.

## Pull requests

- Reference the issue or requirement that motivated the change.
- Note any risk, rollout, or follow-up work.
- Include the local verification steps that were run.
