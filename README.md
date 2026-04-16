# ForgeOps Maintenance Orchestrator

ForgeOps Maintenance Orchestrator is a small, realistic demo repository for showing how teams can move from design intent to engineering requirements, actionable GitHub Issues, guarded code changes, and reviewable pull requests without losing human control.

## Storyline

The fictional ForgeOps platform team converts facility telemetry into actionable maintenance work orders and notifications while applying shared engineering standards across multiple teams.

The repo is intentionally shaped to support an end-to-end workshop:

1. Start with messy kickoff notes.
2. Convert them into requirements, ADRs, and acceptance criteria.
3. Decompose the requirements into actionable issues.
4. Implement one issue with tests and review guardrails.
5. Reuse the same standards and workflows in downstream services.

## Repository tour

```text
.
├─ CONTRIBUTING.md
├─ docs/
│  ├─ meeting-notes/
│  ├─ requirements/
│  ├─ standards/
│  └─ demos/
├─ src/
│  ├─ api/
│  ├─ domain/
│  ├─ rules/
│  ├─ storage/
│  └─ notifications/
├─ tests/
└─ .github/
   ├─ ISSUE_TEMPLATE/
   ├─ PULL_REQUEST_TEMPLATE.md
   ├─ CODEOWNERS
   └─ workflows/
```

## Demo implementation

The included Python + FastAPI service demonstrates the issue-to-PR phase with a small but testable workflow:

- `POST /events` accepts sanitized telemetry events.
- A threshold-based rules engine decides whether maintenance action is required.
- Actionable events create in-memory work orders.
- Every decision writes an audit log entry.
- Actionable events also emit a notification stub.

Additional read-only endpoints expose the generated work orders and audit trail so workshop participants can inspect the flow.

## Quickstart

### Prerequisites

- Python 3.11+

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
```

### Run the service

```bash
uvicorn src.api.main:app --reload
```

### Run quality gates locally

```bash
ruff check .
python -m unittest discover -s tests -v
```

## Example request

```bash
curl -X POST http://127.0.0.1:8000/events \
  -H 'content-type: application/json' \
  -d '{
    "site_id": "site-west-01",
    "asset_id": "compressor-17",
    "metric_name": "bearing_temperature_c",
    "metric_value": 102.4,
    "threshold": 95.0,
    "severity": "critical",
    "observed_at": "2026-04-16T03:00:00Z",
    "metadata": {
      "source": "edge-gateway-1",
      "shift": "night"
    }
  }'
```

## Workshop flow

- Review `/docs/meeting-notes/2026-04-kickoff.md`
- Walk through `/docs/requirements/req-001-orchestrator.md`
- Use the templates in `.github/ISSUE_TEMPLATE/`
- Implement the demo issue in `src/` and validate with `tests/`
- Open a PR using `.github/PULL_REQUEST_TEMPLATE.md`
- Show how `.github/workflows/ci.yml` and `CODEOWNERS` act as guardrails

## License

MIT, see `/LICENSE`.
