from __future__ import annotations

from fastapi import FastAPI

from .models import EventProcessingResult, TelemetryEventIn
from .services import InMemoryStore, process_event

app = FastAPI(title="ForgeOps Maintenance Orchestrator", version="0.1.0")
store = InMemoryStore()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/events", response_model=EventProcessingResult, status_code=202)
def ingest_event(event: TelemetryEventIn) -> EventProcessingResult:
    return process_event(event, store)
