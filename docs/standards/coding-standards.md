# Coding Standards

## Intent

Keep the codebase easy to review live and easy to extend in small steps.

## Rules

- Prefer small modules with one obvious responsibility.
- Keep functions short enough that their branching logic can be understood without scrolling.
- Use descriptive names tied to the domain: `work_order`, `audit_entry`, `correlation_id`.
- Avoid clever abstractions for workshop code. Optimize for readability over framework tricks.
- Validate inputs at the boundary and keep domain logic deterministic.
- Return structured data instead of packing decisions into strings.
- Handle errors explicitly and fail fast on invalid input.
- Keep side effects visible in code paths that write audit or notification records.

## Review Questions

- Is the behavior obvious from function and variable names?
- Does the code map back to a named requirement or acceptance criterion?
- Are generated changes small enough for a reviewer to reason about quickly?