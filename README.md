# ForgeOps Maintenance Orchestrator

ForgeOps Maintenance Orchestrator is a small, workshop-friendly demo repository for a 90-minute session on Agentic SDLC with GitHub Copilot. The scenario is fictional but grounded in an industrial operations story: facility telemetry arrives, rules evaluate equipment health, maintenance work orders are created, audit logs are written, and a notification stub records what would be dispatched next.

The repository is intentionally shaped to demonstrate the whole path from messy meeting notes to requirements, issue breakdown, working code, tests, pull request guardrails, and reusable engineering standards.

## Story Overview

The ForgeOps platform team supports several manufacturing sites. Operators want a lightweight service that turns telemetry anomalies into maintenance work orders fast enough to reduce downtime, but the engineering team also needs traceability, repeatable standards, and human review controls around AI-assisted development.

The workshop flow uses one realistic feature slice:

- A telemetry event is submitted to `POST /events`.
- A simple rule checks whether temperature crosses a threshold.
- A work order is created in memory for triggered events.
- Audit entries are appended for ingestion and decisions.
- A notification stub records what would have been dispatched.

## Architecture

```text
+---------------------+       +------------------+       +-------------------+
| Telemetry Producer  | ----> | FastAPI /events  | ----> | Rule Evaluation   |
| plant gateway / PLC |       | request handling |       | temperature check |
+---------------------+       +------------------+       +-------------------+
                                        |                              |
                                        v                              v
                              +------------------+           +------------------+
                              | In-memory store  |           | Audit log append |
                              | events/workorders|           | decision trail   |
                              +------------------+           +------------------+
                                        |
                                        v
                              +------------------+
                              | Notification stub|
                              | dispatch record  |
                              +------------------+
```

## Quickstart

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the API.
4. Run the quality checks.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
uvicorn forgeops_orchestrator.main:app --app-dir src --reload
```

In a second shell:

```powershell
ruff format --check .
ruff check .
pytest
```

Sample request:

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/events -ContentType application/json -Body '{
  "event_id": "evt-live-001",
  "site_id": "plant-7",
  "asset_id": "compressor-2",
  "metric": "temperature",
  "value": 104.5,
  "severity": "critical",
  "timestamp": "2026-04-15T10:30:00Z",
  "correlation_id": "corr-live-001"
}'
```

## Demo Flow

1. Start with messy notes in `docs/meeting-notes/2026-04-kickoff.md`.
2. Show how requirements and an ADR are derived in `docs/requirements/`.
3. Break the work into issues using `docs/issues/sample-issues.md` and the issue templates.
4. Implement the endpoint and tests in `src/` and `tests/`.
5. Use the PR template, CODEOWNERS, and CI workflow to show review guardrails.
6. Close by showing how standards in `docs/standards/` can be reused in another repo.

## Workshop Agenda

| Time | Segment | Outcome |
| --- | --- | --- |
| 0-10 min | Setup and story | Establish the industrial scenario and guardrail theme |
| 10-25 min | Meeting notes to requirements | Convert ambiguity into user stories and acceptance criteria |
| 25-40 min | Requirements to issues | Create implementation-ready work items |
| 40-70 min | Issue to code and tests | Build the `POST /events` slice with Copilot assistance |
| 70-85 min | PR and quality gates | Show templates, CODEOWNERS, CI, and human review points |
| 85-90 min | Wrap-up | Summarize repeatable practices and next steps |

## Repository Map

- `docs/meeting-notes/` contains the kickoff notes used as the ambiguous starting point.
- `docs/requirements/` contains the requirement spec and ADR.
- `docs/standards/` captures coding, testing, observability, and prompting guidance.
- `docs/demos/` contains facilitator scripts with exact prompts to paste into Copilot Chat.
- `docs/issues/sample-issues.md` provides the 8 issue breakdown used in the workshop.
- `src/forgeops_orchestrator/` contains the FastAPI service and in-memory orchestration logic.
- `tests/` contains the core workshop validation scenarios.
- `.github/` contains issue forms, pull request template, CODEOWNERS, and reusable CI.

## Workshop-Friendly Design Choices

- Python and FastAPI keep the code compact and readable for live explanation.
- The persistence layer is in memory so the repo stays setup-light.
- Audit records and notifications are explicit to support observability and compliance discussion.
- The repository emphasizes review guardrails over automation theater: no auto-merge, no hidden steps, no black-box deployment story.
