# Demo 03: Issue To PR

## Objective

Implement one issue with tests and prepare a reviewable pull request.

## Facilitator Steps

1. Pick the ingestion or rules-engine issue from `docs/issues/sample-issues.md`.
2. Open the relevant application file and test file.
3. Paste the prompt below into Copilot Chat.

## Exact Prompt

```text
Implement the selected ForgeOps issue in the existing Python FastAPI codebase.

Constraints:
- keep the solution small and readable
- preserve the in-memory architecture
- map the implementation to docs/requirements/req-001-orchestrator.md
- add or update pytest coverage for the happy path and one failure or no-action path
- do not introduce a real database or external notification service

After the code change, draft a pull request summary using .github/PULL_REQUEST_TEMPLATE.md with:
- summary
- linked issue
- acceptance criteria mapping
- test evidence
- risk notes
```

## Expected Output

- A focused code change with corresponding tests.
- A PR description that explicitly maps code back to requirements.
- A clear explanation of what still needs human review.

## PR Checklist

- Tests run locally.
- Acceptance criteria are referenced explicitly.
- Logging or audit impact is called out.
- Risk is described, even if low.