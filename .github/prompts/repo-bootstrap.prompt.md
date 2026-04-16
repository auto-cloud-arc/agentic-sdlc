---
name: repo-bootstrap
description: Describe when to use this prompt
agent: agent
model: GPT-5.4 (copilot)
---

<!-- Tip: Use /create-prompt in chat to generate content with agent assistance -->

You are a GitHub Copilot-powered software engineer helping me scaffold a demo repository for a 90-minute workshop on "Agentic SDLC with GitHub Copilot".

Create a repository named "forgeops-maintenance-orchestrator" with a realistic (fictional) Honeywell-style industrial scenario:
- We ingest facility telemetry events
- Evaluate simple rules
- Create maintenance work orders
- Write audit logs
- (Optional) emit notifications via a stub

PRIMARY GOAL:
Demonstrate an end-to-end flow from meeting notes -> requirements -> GitHub Issues -> code + tests -> PR + review guardrails -> reusable standards.

TECH STACK:
Choose ONE workshop-friendly stack and implement minimal working code + tests:
Option A: Python + FastAPI + pytest
Option B: TypeScript + Express + jest
Pick the simplest. Keep the code small and readable.

CREATE THIS REPO STRUCTURE:
- README.md with: story overview, architecture diagram (ASCII is fine), quickstart, demo flow, and workshop agenda.
- docs/meeting-notes/2026-04-kickoff.md containing messy realistic notes (ambiguous statements, NFRs, constraints, open questions).
- docs/requirements/req-001-orchestrator.md derived from notes: goals, non-goals, user stories, acceptance criteria, NFRs, open questions.
- docs/requirements/adr-001-event-model.md: event schema decision + versioning rationale.
- docs/standards/
  - coding-standards.md (naming, structure, small functions, error handling)
  - testing-standards.md (unit vs integration, what to mock, edge cases)
  - observability-standards.md (structured logs, correlation IDs, audit log fields)
  - prompting-playbook.md (recommended Copilot prompts, good vs bad examples, safety: never auto-merge, always verify)
- docs/demos/
  - demo-01-meeting-to-requirements.md (script + prompts + expected outputs)
  - demo-02-requirements-to-issues.md (script + prompts + expected issue breakdown)
  - demo-03-issue-to-pr.md (script + prompts + PR checklist)
  - demo-04-standards-guardrails.md (script + prompts)
- src/ minimal working app with:
  - POST /events (ingest)
  - rule evaluation (e.g., temperature > threshold triggers)
  - persistence (in-memory ok for workshop)
  - audit logging (append-only list/file ok)
- tests/ with at least:
  - happy path test creates work order
  - invalid event rejected
  - audit log entry written
- .github/
  - ISSUE_TEMPLATE/ feature.yml, bug.yml, tech-debt.yml, adr-request.yml (include fields for AC, test plan, logging/telemetry, rollout risks)
  - PULL_REQUEST_TEMPLATE.md that forces: summary, linked issue, AC mapping, test evidence, risk notes
  - CODEOWNERS with at least one sample ownership rule
  - workflows/
    - ci.yml running format/lint/tests
    - reusable-quality-gates.yml using workflow_call for reuse
- CONTRIBUTING.md describing: branching, commit style, running tests, PR expectations
- Add placeholder LICENSE (MIT ok)

WORKSHOP DEMO REQUIREMENTS:
- Include a sample list of 6-8 GitHub Issues in docs (or as markdown) that map to the requirements: ingestion endpoint, rules engine, persistence/work orders, audit log, notification stub, CI/standards, observability, ADR request.
- Ensure each demo script contains exact Copilot prompts I can paste during the workshop.

OUTPUT:
Generate all files with substantive content (not placeholders). Keep code minimal but runnable.