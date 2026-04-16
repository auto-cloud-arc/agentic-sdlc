# Demo 03: Issue to pull request

## Goal

Implement one issue end to end while showing that humans stay in control.

## Live flow

1. Open the feature issue for `POST /events`.
2. Ask Copilot to scaffold the API handler, orchestration service, and tests within the issue boundaries.
3. Review the generated code for correctness, readability, and acceptance-criteria coverage.
4. Run linting and tests.
5. Open a PR using the template in `.github/PULL_REQUEST_TEMPLATE.md`.

## Reviewer checklist

- Do the code changes map back to the acceptance criteria?
- Are failure paths covered?
- Is PII rejected?
- Is auditability preserved?
- Are follow-up items called out instead of silently deferred?
