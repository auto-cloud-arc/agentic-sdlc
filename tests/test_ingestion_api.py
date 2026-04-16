import unittest

from fastapi.testclient import TestClient

from src.api.main import create_app


class IngestionApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(create_app())

    def test_actionable_event_creates_work_order_notification_and_audit_entry(self) -> None:
        response = self.client.post(
            "/events",
            json={
                "site_id": "site-west-01",
                "asset_id": "compressor-17",
                "metric_name": "bearing_temperature_c",
                "metric_value": 102.4,
                "threshold": 95.0,
                "severity": "critical",
                "observed_at": "2026-04-16T03:00:00Z",
                "metadata": {"source": "edge-gateway-1", "shift": "night"},
            },
        )

        self.assertEqual(response.status_code, 202)
        payload = response.json()
        self.assertTrue(payload["decision"]["action_required"])
        self.assertEqual(payload["decision"]["priority"], "high")
        self.assertIsNotNone(payload["work_order"])
        self.assertIsNotNone(payload["notification"])

        audit_response = self.client.get("/audit-log")
        self.assertEqual(audit_response.status_code, 200)
        self.assertEqual(len(audit_response.json()), 1)

    def test_non_actionable_event_only_records_audit_entry(self) -> None:
        response = self.client.post(
            "/events",
            json={
                "site_id": "site-east-02",
                "asset_id": "pump-04",
                "metric_name": "vibration_mm_s",
                "metric_value": 3.2,
                "threshold": 4.5,
                "severity": "warning",
                "observed_at": "2026-04-16T03:05:00Z",
                "metadata": {"source": "edge-gateway-2"},
            },
        )

        self.assertEqual(response.status_code, 202)
        payload = response.json()
        self.assertFalse(payload["decision"]["action_required"])
        self.assertIsNone(payload["work_order"])
        self.assertIsNone(payload["notification"])

        work_orders_response = self.client.get("/work-orders")
        self.assertEqual(work_orders_response.status_code, 200)
        self.assertEqual(work_orders_response.json(), [])

    def test_pii_metadata_is_rejected(self) -> None:
        response = self.client.post(
            "/events",
            json={
                "site_id": "site-east-02",
                "asset_id": "pump-04",
                "metric_name": "vibration_mm_s",
                "metric_value": 7.5,
                "threshold": 4.5,
                "severity": "warning",
                "observed_at": "2026-04-16T03:05:00Z",
                "metadata": {"email": "operator@example.com"},
            },
        )

        self.assertEqual(response.status_code, 422)
        self.assertIn("PII is not allowed", response.text)


if __name__ == "__main__":
    unittest.main()
