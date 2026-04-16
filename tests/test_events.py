from fastapi.testclient import TestClient

from forgeops_orchestrator.main import app, store

client = TestClient(app)


def setup_function() -> None:
    store.reset()


def test_happy_path_creates_work_order() -> None:
    response = client.post(
        "/events",
        json={
            "event_id": "evt-1001",
            "site_id": "plant-7",
            "asset_id": "compressor-2",
            "metric": "temperature",
            "value": 104.5,
            "severity": "critical",
            "timestamp": "2026-04-15T10:30:00Z",
            "correlation_id": "corr-demo-1001",
        },
    )

    assert response.status_code == 202
    payload = response.json()
    assert payload["decision"]["triggered"] is True
    assert payload["work_order"]["asset_id"] == "compressor-2"
    assert payload["notification_emitted"] is True
    assert len(store.work_orders) == 1


def test_invalid_event_rejected() -> None:
    response = client.post(
        "/events",
        json={
            "event_id": "evt-1002",
            "site_id": "p1",
            "asset_id": "compressor-2",
            "metric": "humidity",
            "value": 70,
            "severity": "warning",
            "timestamp": "2026-04-15T10:31:00Z",
        },
    )

    assert response.status_code == 422
    assert store.work_orders == []
    assert store.audit_entries == []


def test_audit_log_entry_written() -> None:
    response = client.post(
        "/events",
        json={
            "event_id": "evt-1003",
            "site_id": "plant-7",
            "asset_id": "pump-4",
            "metric": "pressure",
            "value": 42,
            "severity": "info",
            "timestamp": "2026-04-15T10:32:00Z",
            "correlation_id": "corr-demo-1003",
        },
    )

    assert response.status_code == 202
    assert len(store.audit_entries) == 2
    assert store.audit_entries[0].action == "event_ingested"
    assert store.audit_entries[1].outcome == "no_action"
