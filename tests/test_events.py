from fastapi.testclient import TestClient

from src.main import app, audit_log_store, work_orders_store

client = TestClient(app)


def setup_function() -> None:
    client.post("/reset")


def test_happy_path_creates_work_order() -> None:
    payload = {
        "event_id": "evt-1001",
        "facility_id": "plant-7",
        "asset_id": "boiler-3",
        "event_type": "telemetry.temperature",
        "metric": "temperature",
        "value": 121.0,
        "threshold": 100.0,
        "timestamp": "2026-04-16T02:00:00Z",
        "correlation_id": "corr-123",
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["work_order_created"] is True
    assert body["work_order_id"].startswith("WO-")
    assert len(work_orders_store) == 1


def test_invalid_event_rejected() -> None:
    payload = {
        "event_id": "evt-1002",
        "facility_id": "plant-7",
        "asset_id": "boiler-3",
        "event_type": "telemetry.temperature",
        "metric": "temperature",
        "value": 85.0,
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 422


def test_audit_log_entry_written() -> None:
    payload = {
        "event_id": "evt-1003",
        "facility_id": "plant-9",
        "asset_id": "chiller-2",
        "event_type": "telemetry.temperature",
        "metric": "temperature",
        "value": 95.0,
        "threshold": 90.0,
        "timestamp": "2026-04-16T02:05:00Z",
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 200
    assert any(item["action"] == "event_ingested" for item in audit_log_store)
    assert any(item["action"] == "work_order_created" for item in audit_log_store)
