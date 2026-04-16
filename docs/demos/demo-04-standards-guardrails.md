# Demo 04: Standards And Guardrails

## Objective

Show that standards and review controls are first-class artifacts, not verbal reminders.

## Facilitator Steps

1. Open `docs/standards/` and `.github/` side by side.
2. Show the reusable workflow, PR template, and CODEOWNERS file.
3. Paste the prompt below into Copilot Chat.

## Exact Prompt

```text
Review this repository for Agentic SDLC guardrails.

Summarize how the following artifacts work together and identify any obvious gaps:
- docs/standards/coding-standards.md
- docs/standards/testing-standards.md
- docs/standards/observability-standards.md
- docs/standards/prompting-playbook.md
- .github/PULL_REQUEST_TEMPLATE.md
- .github/CODEOWNERS
- .github/workflows/reusable-quality-gates.yml

Keep the answer concise and oriented toward a workshop audience learning how to keep Copilot-assisted changes reviewable.
```

## Expected Output

- A concise explanation of how standards, templates, and CI work together.
- A reminder that human review remains the merge gate.
- A concrete example of guardrails being reusable across multiple repositories.