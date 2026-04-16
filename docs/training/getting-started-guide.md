# Getting Started Guide

This guide is the detailed companion to the repository [README.md](../../README.md). Read the README first for the high-level story, architecture, and workshop framing, then use this document when you want the setup and first-run workflow to be explicit and low-friction.

## Who This Guide Is For

- New contributors opening the repository for the first time.
- Workshop participants who want a step-by-step path instead of a short quickstart.
- Facilitators who need a predictable way to verify that the demo works before teaching with it.

## What You Are Setting Up

This repository is a small FastAPI service that demonstrates an Agentic SDLC workflow around one realistic feature slice:

- receive a telemetry event at `POST /events`
- evaluate a simple temperature rule
- create an in-memory work order when the rule triggers
- write audit entries for ingestion and rule outcome
- record a notification stub instead of calling an external service

The code is intentionally small so you can understand the full loop from notes to requirements to issues to implementation to tests.

## Recommended Reading Order

If you are new to the repo, use this order:

1. [README.md](../../README.md)
2. [docs/meeting-notes/2026-04-kickoff.md](../meeting-notes/2026-04-kickoff.md)
3. [docs/requirements/req-001-orchestrator.md](../requirements/req-001-orchestrator.md)
4. [docs/issues/sample-issues.md](../issues/sample-issues.md)
5. [src/forgeops_orchestrator/main.py](../../src/forgeops_orchestrator/main.py)
6. [src/forgeops_orchestrator/services.py](../../src/forgeops_orchestrator/services.py)
7. [tests/test_events.py](../../tests/test_events.py)
8. [CONTRIBUTING.md](../../CONTRIBUTING.md)

That sequence mirrors the workshop flow and makes the repository easier to understand than starting in the code alone.

## Repository Orientation

Use this mental model when exploring the tree:

- [README.md](../../README.md): high-level overview, architecture, quickstart, and workshop framing.
- [run_server.py](../../run_server.py): local development launcher for the API.
- [src/forgeops_orchestrator/](../../src/forgeops_orchestrator): application package.
- [tests/](../../tests): pytest coverage for the workshop-critical behavior.
- [docs/meeting-notes/](../meeting-notes): the intentionally messy starting artifact.
- [docs/requirements/](../requirements): requirements and ADRs derived from the notes.
- [docs/issues/](../issues): implementation-ready issue examples.
- [docs/demos/](../demos): facilitator prompts and demo scripts.
- [docs/standards/](../standards): coding, testing, observability, and prompting guardrails.
- [CONTRIBUTING.md](../../CONTRIBUTING.md): branching, commits, test commands, and review expectations.

## Prerequisites

Before you run anything, confirm that you have:

- Python 3.12 or later available on your machine.
- PowerShell available if you want to follow the command examples exactly.
- Network and local security settings that allow binding to a localhost port.

This repository does not require Docker, a database, or any external services for local execution.

## First-Time Setup

Open a terminal in the repository root and run each command in order.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

What these commands do:

- `python -m venv .venv` creates an isolated local Python environment.
- `Activate.ps1` switches the shell into that environment.
- `pip install --upgrade pip` updates the installer itself.
- `pip install -r requirements-dev.txt` installs both runtime and development dependencies.

You should expect the virtual environment name, such as `(.venv)`, to appear in your prompt after activation.

## Start The API

From the repository root, run:

```powershell
python run_server.py --reload
```

Why this command matters:

- It is the repository-supported way to start the app locally.
- It enables reload behavior for development.
- It prefers port `8000`.
- If port `8000` is already occupied, it automatically falls back to `8001` and prints the selected URL.

Typical startup output looks like this:

```text
Starting ForgeOps API at http://127.0.0.1:8000
```

Or, if `8000` is unavailable:

```text
Port 8000 is unavailable; starting on 8001 instead.
Starting ForgeOps API at http://127.0.0.1:8001
```

If you need to choose your own port explicitly, use:

```powershell
python run_server.py --reload --port 8010
```

## Verify The Server Is Up

Open a second terminal in the repository root, activate the virtual environment again, and call the health endpoint.

If the server started on `8000`:

```powershell
.\.venv\Scripts\Activate.ps1
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8000/health
```

If the server started on `8001`:

```powershell
.\.venv\Scripts\Activate.ps1
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8001/health
```

Expected response:

```json
{"status":"ok"}
```

If you get a connection refusal, the API is not currently running on that port. Re-check the terminal where you started `run_server.py` and use the exact URL it printed.

## Send A Sample Event

Once the health check works, send a realistic event to the API.

If the server is running on `8000`:

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

If the server is running on `8001`, replace `8000` with `8001` in the URL.

What to expect from the response:

- HTTP status `202`
- a decision object showing the rule triggered
- a generated or preserved `correlation_id`
- a `work_order` object
- `notification_emitted` set to `true`

## Run Local Quality Checks

When you are done confirming the API works, run the same checks used in the repository guidance and CI workflow.

```powershell
ruff format --check .
ruff check .
pytest
```

These commands are aligned with [CONTRIBUTING.md](../../CONTRIBUTING.md) and the reusable workflow in [.github/workflows/reusable-quality-gates.yml](../../.github/workflows/reusable-quality-gates.yml).

## How To Understand The Code Quickly

If you want a fast mental model of the implementation, use this sequence:

1. Read [src/forgeops_orchestrator/main.py](../../src/forgeops_orchestrator/main.py) to see the API surface.
2. Read [src/forgeops_orchestrator/models.py](../../src/forgeops_orchestrator/models.py) to understand the payloads and return types.
3. Read [src/forgeops_orchestrator/services.py](../../src/forgeops_orchestrator/services.py) to see the business behavior.
4. Read [tests/test_events.py](../../tests/test_events.py) to see the expected outcomes in executable form.

That progression keeps the implementation readable and avoids starting with lower-level details too early.

## How To Understand The Workshop Flow Quickly

If your goal is to understand the training value of the repo rather than only running the API, walk the documentation in this order:

1. [docs/meeting-notes/2026-04-kickoff.md](../meeting-notes/2026-04-kickoff.md)
2. [docs/requirements/req-001-orchestrator.md](../requirements/req-001-orchestrator.md)
3. [docs/requirements/adr-001-event-model.md](../requirements/adr-001-event-model.md)
4. [docs/issues/sample-issues.md](../issues/sample-issues.md)
5. [docs/demos/](../demos)
6. [docs/standards/](../standards)
7. [.github/PULL_REQUEST_TEMPLATE.md](../../.github/PULL_REQUEST_TEMPLATE.md)

This shows how the repository teaches traceability and guardrails, not just coding.

## Common First-Day Questions

### Why use `python run_server.py --reload` instead of raw `uvicorn`?

Because this repository now includes a small launcher that handles the common Windows case where port `8000` is already in use. It avoids forcing every new user to debug the same bind error manually.

### Why is everything in memory?

Because the repository is optimized for a 90-minute workshop. In-memory storage keeps setup fast and the architecture small enough to explain live.

### Why are there so many docs for such a small service?

Because the repository is teaching an Agentic SDLC workflow. The notes, requirements, issues, standards, templates, and tests are all part of the lesson.

## Troubleshooting

### The server says port `8000` is unavailable

This is expected on some Windows machines. The launcher should automatically start on `8001`. Use the printed URL for health checks and sample requests.

### `Invoke-RestMethod` says the connection was refused

Usually one of these is true:

- the API is not currently running
- you are calling `8000` even though the launcher switched to `8001`
- the terminal that started the API exited or failed

Read the startup terminal first and use the exact port it printed.

### `pytest` cannot import the application package

Run tests from the repository root, not from inside `src/` or `tests/` individually. The repository already includes test path setup under [tests/conftest.py](../../tests/conftest.py).

### I changed code but do not know what to validate

Start with:

- `ruff format --check .`
- `ruff check .`
- `pytest`

Then map your change back to the relevant acceptance criteria in [docs/requirements/req-001-orchestrator.md](../requirements/req-001-orchestrator.md).

## Suggested First Contributions

If you are using this repository to practice contributing, reasonable first changes include:

1. Add a new test around threshold boundary behavior.
2. Tighten or clarify documentation in one of the standards files.
3. Extend the sample issues with a small follow-up item.
4. Improve a demo script while preserving the current workshop scope.

Keep changes small, run the local checks, and follow the contribution expectations in [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Summary

Use [README.md](../../README.md) for the high-level view and this guide for the explicit first-run path. If you can create the virtual environment, install dependencies, start `python run_server.py --reload`, pass the health check, post one sample event, and run `pytest`, you are fully set up to explore or contribute.