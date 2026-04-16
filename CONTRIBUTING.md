# Contributing

## Branching
- Create short-lived branches per issue (e.g., `feature/events-ingest`).
- Keep pull requests focused and small.

## Commit style
- Use imperative commit messages (e.g., `Add event ingestion endpoint`).
- Prefer one logical change per commit.

## Running checks locally
```bash
pip install -r requirements-dev.txt
ruff format --check .
ruff check .
pytest
```

## Pull request expectations
- Link a GitHub Issue.
- Map acceptance criteria to code/test evidence.
- Document telemetry impact and rollout risks.
- Require human review before merge.
