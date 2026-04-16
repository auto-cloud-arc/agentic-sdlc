# Coding Standards

## Principles
- Keep functions small and single-purpose.
- Prefer explicit names (`ingest_event`, `append_audit`) over abstractions.
- Use type hints for function signatures.
- Fail fast with framework validation for malformed input.

## Structure
- Place API entrypoint in `src/main.py`.
- Keep workshop logic in pure functions where possible (`should_create_work_order`).
- Keep shared mutable state isolated and easy to reset for tests.

## Error handling
- Use FastAPI/Pydantic validation for request errors.
- Return clear API response models.
- Never swallow exceptions silently.
