# Testing Standards

## Test levels
- **Unit-style**: exercise rule logic and data validation expectations.
- **Integration-style**: use FastAPI `TestClient` to verify endpoint behavior.

## Mocking guidance
- Do not mock rule logic or in-memory persistence for this workshop.
- Only mock external integrations if added later (e.g., real notification providers).

## Minimum edge cases
- Valid event triggers work order creation.
- Invalid event payload is rejected.
- Audit logging occurs for key actions.
- Non-triggering event does not create work order.
