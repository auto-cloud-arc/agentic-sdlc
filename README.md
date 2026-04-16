# Agentic Devops

> **Goal:** Turn "design intent -> engineering requirements -> actionable GitHub Issues -> code + PRs (with humans in control)" into a smooth, realistic storyline you can demo end-to-end.
>
> **Note:** The scenario below is fictional and sanitized. It is designed to feel like a Contoso industrial software workflow without using confidential content.

---

## 1. Cohesive Story-Quality Scenario

### The product: **ForgeOps Maintenance Orchestrator**

A small internal platform team builds a service that converts facility telemetry into **actionable maintenance work orders** and **notifications**, while enforcing shared engineering standards across multiple teams.

#### Why this story works for the topics

- It naturally starts with **meetings and design notes** as ambiguous inputs.
- It forces **requirements and acceptance criteria** to get crisp.
- It yields multiple **small issues** that are well suited to Copilot-assisted coding and PR workflows.
- It benefits from **org-wide standards** and reusable guardrails such as linters, tests, workflows, and templates.

### The cast

- **Product Owner (PO):** cares about uptime, auditability, and fast triage.
- **Site Reliability Engineer (SRE):** cares about alerts, reliability, and runbooks.
- **Backend Developer:** builds ingestion and the rules engine.
- **Platform Engineer:** enforces standards, workflows, and reusable templates.
- **Reviewer or Lead:** provides human-in-the-loop decisions and approvals.

### The problem statement

> "We are missing critical maintenance events because design intent gets lost between meetings and tickets. We need a repeatable way to convert discussions into requirements, issues, code, and guarded PRs without slowing down developers."

---

## 2. Enriched Topic Outline and Subtopics

Each section below preserves your original intent while adding practical subtopics and demo hooks.

### A. Design / Meeting -> Clear Engineering Requirements

#### Subtopics to include

- Turning meeting notes into:
  - **Problem statement**
  - **Non-functional requirements** such as latency, reliability, and audit logging
  - **Constraints** such as no PII, retention, and dependency boundaries
  - **Assumptions and open questions**
- Converting ambiguous statements into **testable acceptance criteria**
- Capturing architecture decisions as lightweight **ADRs**
- Aligning on a **definition of done** that covers tests, docs, and observability

#### Demo hook

- Start from `/docs/meeting-notes/2026-04-xx-kickoff.md` with messy notes.
- Use Copilot to produce `/docs/requirements/req-001-maintenance-orchestrator.md`.

---

### B. Requirements -> Actionable GitHub Issues

#### Subtopics to include

- Issue decomposition: **Epic -> Features -> Tasks**
- Issue templates for:
  - Feature
  - Bug
  - Tech debt
  - ADR request
- Writing issues with:
  - **Scope**
  - **Acceptance Criteria**
  - **Telemetry and logging expectations**
  - **Test plan**
  - **Risk and rollout notes**
- Labels, milestones, and lightweight project board automation

#### Demo hook

- Copilot transforms requirements into 6 to 8 issues using templates under:
  - `.github/ISSUE_TEMPLATE/feature.yml`
  - `.github/ISSUE_TEMPLATE/bug.yml`

---

### C. Issues -> Code with Human Control

#### Subtopics to include

- Copilot-assisted implementation patterns:
  - Scaffolding endpoints and handlers
  - Generating unit and integration tests
  - Refactoring and explaining code
- Human-control practices:
  - Explicit prompt boundaries
  - Review checklists
  - PR descriptions that cite acceptance criteria
  - "Trust but verify" through tests, linting, and static checks

#### Demo hook

- Implement one issue end to end:
  - Telemetry ingestion endpoint
  - Rules evaluation
  - Work order creation
  - Tests
  - Open PR and review

---

### D. Making Team Standards Explicit

#### Subtopics to include

- Standards as code:
  - `CONTRIBUTING.md`
  - `docs/standards/coding-standards.md`
  - `docs/standards/testing-standards.md`
  - `docs/standards/observability.md`
- PR templates and review checklists
- Definition of done enforced by CI:
  - Formatting
  - Linting
  - Tests
  - Optional coverage thresholds
- Prompting standards:
  - House-style prompts for Copilot Chat
  - Examples of good and bad prompts

#### Demo hook

- Show "Before: tribal knowledge" and "After: visible, repeatable rules."

---

### E. Reusing Standards Across Teams

#### Subtopics to include

- Reusable GitHub Actions workflows with `workflow_call`
- Repo templates with a cookiecutter-style structure
- Shared issue templates and PR templates
- `CODEOWNERS` for consistent review routing

#### Demo hook

- A second downstream service folder or sample repo branch uses the same workflow and standards with minimal work.

---

### F. Guardrails and Review, Not Blind Automation

#### Subtopics to include

- Protected branches and required checks
- Required reviewers through `CODEOWNERS`
- CI gates and manual approvals where they matter
- Minimal-risk rollout:
  - Feature flags through simple configuration
  - Simulated staged environments
- AI-safety guardrails:
  - Never auto-merge
  - Always run tests
  - Require PR descriptions to map back to acceptance criteria

#### Demo hook

- Copilot proposes changes, and you show how checks and review prevent risky merges.

---

### G. From Inconsistent Practices to Shared Ways of Working

#### Subtopics to include

- Team agreements encoded as templates and automation
- Onboarding path:
  - Quickstart
  - First PR in 15 minutes
- Repeatable cadence:
  - Meeting -> requirements -> issues -> PRs

#### Demo hook

- A new developer follows the README and templates to deliver a feature consistently.

---

### H. What Success Looks Like for Developers

#### Subtopics to include

- Leading indicators:
  - Fewer clarification loops
  - PR turnaround time
  - Fewer reopened issues
  - Increased test coverage on new code
- Qualitative outcomes:
  - Consistent code style
  - Predictable reviews
  - Faster onboarding

#### Demo hook

- Close the session with a before-and-after storyboard and a short checklist teams can adopt next week.

---

## 3. 90-Minute Session Run of Show

### 0-10 min: Setup and the Agentic SDLC why

- The pain: intent gets lost from meeting -> tickets -> code.
- The promise: convert artifacts efficiently while keeping humans in control.
- Introduce the repo and storyline.

### 10-25 min: Meeting notes -> Requirements

#### Live demo

- Open `/docs/meeting-notes/kickoff.md`.
- Use Copilot Chat to produce:
  - Requirements doc
  - Acceptance criteria
  - Open questions
  - ADR stub

### 25-40 min: Requirements -> GitHub Issues

#### Live demo

- Use Copilot to generate 6 to 8 issues aligned to templates:
  - Ingestion endpoint
  - Rules engine
  - Persistence layer
  - Audit log
  - Notification stub
  - Tests and CI
- Show crisp scope and acceptance criteria in each issue.

### 40-70 min: Issue -> Code + Tests + PR

#### Live demo

- Implement 1 to 2 issues with Copilot assistance.
- Generate tests.
- Open a PR using a template that maps changes back to acceptance criteria.
- Walk through reviewer flow and show why guardrails matter.

### 70-85 min: Standards, reuse, and guardrails

- Show `.github/workflows/ci.yml` gates.
- Show the reusable workflow structure.
- Show standards docs and `CODEOWNERS`.

### 85-90 min: Wrap up

- Reiterate outcomes: fewer surprises, faster onboarding, and more predictable quality.
- Leave a short next-steps checklist.

---

## 4. The Demo Repo You Will Build

Use this as the **repository blueprint** for your workshop.

```text
forgeops-maintenance-orchestrator/
├─ README.md
├─ docs/
│  ├─ meeting-notes/
│  │  └─ 2026-04-kickoff.md
│  ├─ requirements/
│  │  ├─ req-001-orchestrator.md
│  │  └─ adr-001-event-model.md
│  ├─ standards/
│  │  ├─ coding-standards.md
│  │  ├─ testing-standards.md
│  │  ├─ observability-standards.md
│  │  └─ prompting-playbook.md
│  └─ demos/
│     ├─ demo-01-meeting-to-requirements.md
│     ├─ demo-02-requirements-to-issues.md
│     ├─ demo-03-issue-to-pr.md
│     └─ demo-04-standards-guardrails.md
├─ src/
│  ├─ api/
│  ├─ domain/
│  ├─ rules/
│  ├─ storage/
│  └─ notifications/
├─ tests/
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ feature.yml
│  │  ├─ bug.yml
│  │  ├─ tech-debt.yml
│  │  └─ adr-request.yml
│  ├─ PULL_REQUEST_TEMPLATE.md
│  ├─ CODEOWNERS
│  └─ workflows/
│     ├─ ci.yml
│     └─ reusable-quality-gates.yml
├─ CONTRIBUTING.md
└─ LICENSE
```

### Recommended tech stack

Pick one stack to keep the flow smooth.

#### Option A: Python + FastAPI

- Simple endpoints, fast tests, and easy explanations
- Good for showing Copilot generating tests and refactors quickly

#### Option B: TypeScript + Express

- Similar benefits
- Strong typing helps demonstrate Copilot patterns

> If Contoso developers skew heavily toward .NET or Java, you can still keep the repo small and concept-driven. The SDLC storyline is the point.

---

## 5. Cohesive Demo Scenarios

### Scenario 1: Kickoff meeting chaos -> crisp requirements

**Artifact:** `/docs/meeting-notes/2026-04-kickoff.md`

Include realistic messy notes such as:

- Need alerts for critical events
- Audit log required
- No PII
- Latency under 2 seconds for event-to-ticket
- Must support multiple sites
- Need to standardize across teams

#### Copilot outputs

- Requirements doc with:
  - Goals and non-goals
  - User stories
  - Acceptance criteria
  - NFRs
  - Open questions
- ADR stub defining the event schema

---

### Scenario 2: Requirements -> GitHub Issues engineers can implement

#### Artifacts

- Issue templates in `.github/ISSUE_TEMPLATE/*`
- 6 to 8 issues created from `req-001`

#### Example issue set

1. **Feature:** Telemetry ingestion endpoint with `POST /events`
2. **Feature:** Rules engine using threshold-based evaluation
3. **Feature:** Work order creation and persistence
4. **Feature:** Audit log entries for each decision
5. **Feature:** Notification stub with simulated email or webhook behavior
6. **Quality:** CI pipeline and standards gates
7. **Tech debt:** Structured logging and correlation IDs
8. **ADR request:** Confirm event schema and versioning approach

Each issue includes:

- Scope
- Acceptance criteria
- Test plan
- Logging expectations

---

### Scenario 3: Issue -> Code + Tests + PR

#### Flow

- Copilot generates:
  - API handler skeleton
  - Domain model
  - Tests for happy path and failure path
- You manually validate:
  - Edge cases
  - Correctness
  - Readability
  - Alignment with standards
- Open PR:
  - PR template forces acceptance criteria mapping
  - CI runs
  - Reviewer sign-off is required

---

### Scenario 4: Standards reused across teams and guardrails

#### Artifacts

- `docs/standards/*`
- `.github/workflows/reusable-quality-gates.yml`
- `CODEOWNERS`
- Documented branch-protection recommendations

#### Demo moment

- Show how a second module or service can adopt the same templates and workflows with almost no extra effort.

---

## 6. Demos as Markdown Scripts

Create facilitator scripts so the session runs consistently.

### `/docs/demos/demo-01-meeting-to-requirements.md`

- Starting state: messy meeting notes
- Live prompts to run in Copilot Chat
- Expected output sections

### `/docs/demos/demo-02-requirements-to-issues.md`

- Prompt to create an epic and decomposed issues
- How to apply labels and milestones

### `/docs/demos/demo-03-issue-to-pr.md`

- Implement Issue #X
- Prompts for code and tests
- PR template mapping to acceptance criteria
- Review checklist

### `/docs/demos/demo-04-standards-guardrails.md`

- Show standards docs
- Show reusable workflows
- Show required checks and review gates

## 8. Bonus: In-Workshop Prompts

These are short, reliable prompts you can use live and also place in `prompting-playbook.md`.

### Prompt: Meeting notes -> Requirements

```text
Convert these meeting notes into an engineering requirements doc.
Include: goals, non-goals, user stories, acceptance criteria, NFRs, constraints, open questions, and a short definition of done.
Keep it concise and testable.
```

### Prompt: Requirements -> Issue breakdown

```text
Decompose this requirements doc into an Epic and 6-8 GitHub issues.
For each issue include: scope, acceptance criteria, test plan, logging/telemetry expectations, and risk/rollout notes.
```

### Prompt: Implement an issue with tests

```text
Implement Issue #<n> following our coding and testing standards.
Create small functions, include error handling, and add unit tests for happy path + one failure path.
Explain any assumptions.
```

### Prompt: PR description with human control

```text
Draft a PR description that links to the issue, maps changes to each acceptance criterion, lists tests executed, calls out risks, and includes a reviewer checklist.
```

---

## 9. Two Choices to Tailor This Further

1. **Preferred language stack for Honeywell developers:** Python, TypeScript, Java, or .NET?
2. **Preferred storyline:**
   - Connected facilities or building controls
   - Aerospace or avionics telemetry
   - Manufacturing line monitoring