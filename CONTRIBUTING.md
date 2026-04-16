# Contributing

## Branching

- Create short-lived branches from `main` using `feature/`, `fix/`, `docs/`, or `chore/` prefixes.
- Keep each branch aligned to one issue or one reviewable change set.
- Rebase or merge `main` before opening a pull request if the branch has drifted.

## Commit Style

- Prefer small commits with intent-first messages, such as `feat: add event ingestion endpoint`.
- Keep generated documentation changes separate from application behavior changes when practical.
- Reference the issue number in the commit body when the relationship is not obvious.

## Local Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Running Tests And Checks

```powershell
ruff format --check .
ruff check .
pytest
```

## Pull Request Expectations

- Link the issue or requirement that drove the change.
- Map the implementation back to acceptance criteria.
- Include test evidence from local runs or CI.
- Call out operational or rollout risk, even when the answer is `low`.
- Note any logging, telemetry, or audit trail impact.
- Keep a human reviewer in the loop for design and merge decisions.

## Copilot Expectations

- Use Copilot to draft, decompose, and accelerate, not to bypass review.
- Validate generated code against the standards in `docs/standards/`.
- Never auto-merge AI-authored changes.
- Prefer prompts that name the file, objective, constraints, and acceptance criteria.