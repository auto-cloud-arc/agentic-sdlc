# Testing Standards

## Test Layers

- Unit tests cover pure rule evaluation and helper behavior.
- Integration-style API tests cover request validation and orchestration through `POST /events`.

## What To Mock

- Do not mock the in-memory store in the main workshop tests.
- Keep notification behavior as a stubbed in-memory record, not a mocked HTTP client.
- Mock only when introducing external boundaries in future iterations.

## Minimum Expectations

- Every new behavior change must include at least one success-path test.
- Validation and edge-case behavior must be tested when input contracts change.
- Audit and logging side effects must be asserted for decision-making code.

## Edge Cases To Remember

- Threshold boundary values.
- Missing or malformed payload fields.
- Non-triggering events that should still be accepted and audited.
- Correlation ID generation when the caller omits it.