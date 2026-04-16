# forgeops-maintenance-orchestrator

Demo repository for a 90-minute workshop: **Agentic SDLC with GitHub Copilot**.

## Story overview
ForgeOps manages industrial facilities with aging HVAC and process-cooling assets. Telemetry arrives from edge gateways. When unsafe temperature readings appear, the orchestrator creates maintenance work orders and writes auditable records for compliance reviews.

## Architecture (ASCII)
```text
+-------------------+      POST /events      +-----------------------------+
| Telemetry Source  | ---------------------> | FastAPI Orchestrator        |
| (gateway/sensor)  |                        | - validate event            |
+-------------------+                        | - evaluate rules            |
                                             | - create work order         |
                                             | - append audit log          |
                                             | - optional notify stub      |
                                             +--------------+--------------+
                                                            |
                                       +--------------------+--------------------+
                                       |                                         |
                           +-----------v-----------+                 +-----------v-----------+
                           | In-memory Event Store |                 | In-memory Work Orders |
                           +-----------------------+                 +-----------------------+
                                                            +-----------------------+
                                                            | In-memory Audit Log    |
                                                            +-----------------------+
```

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn src.main:app --reload
```

Run tests:
```bash
pytest
```

## Demo flow
1. Review messy kickoff notes in `docs/meeting-notes/2026-04-kickoff.md`.
2. Derive requirements and ADRs in `docs/requirements/`.
3. Break requirements into actionable GitHub Issues using templates.
4. Implement issue slices in code + tests (`src/`, `tests/`).
5. Open PR with mandatory AC mapping and risk notes.
6. Enforce standards with reusable CI quality gates.

## Workshop agenda (90 minutes)
- **0-10 min**: Scenario intro and expected outcomes
- **10-25 min**: Meeting notes -> requirements + ADR
- **25-40 min**: Requirements -> GitHub Issues + templates
- **40-65 min**: Issue implementation with Copilot (code + tests)
- **65-80 min**: PR guardrails, CODEOWNERS, reusable CI
- **80-90 min**: Retrospective and next-step automation ideas
