"""
app/main.py — Minimal FastAPI app with Prometheus metrics.

WHY THIS EXISTS
---------------
We need a simple, controllable service to demonstrate:
- success & failure paths (adjustable error rate and latency)
- export of Prometheus metrics for alerting/dashboards

Keep this file short and documented. No extra routes or helpers.
"""
import os, random, time
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Minimal Demo API")

# Metrics: total requests, errors, and latency histogram
REQS = Counter("requests_total", "Total HTTP requests", ["route"])
ERRS = Counter("errors_total", "Total HTTP 5xx errors", ["route"])
LAT = Histogram("request_latency_seconds", "Latency in seconds", ["route"])

# Control behavior via env vars for live incident rehearsal
ERROR_RATE = float(os.getenv("ERROR_RATE", "0.0"))  # 0.0 to 1.0
SLEEP_MS = int(os.getenv("SLEEP_MS", "0"))          # artificial latency in ms

@app.get("/")
def root():
    """
    Simple healthy endpoint. Metrics include latency and error rate.
    Tune ERROR_RATE/SLEEP_MS via environment variables or docker compose updates.
    """
    route = "/"
    start = time.time()
    try:
        if SLEEP_MS > 0:
            time.sleep(SLEEP_MS / 1000.0)
        if random.random() < ERROR_RATE:
            ERRS.labels(route=route).inc()
            return Response("internal error", status_code=500)
        return {"ok": True, "message": "hello from demo"}
    finally:
        LAT.labels(route=route).observe(time.time() - start)
        REQS.labels(route=route).inc()

@app.get("/metrics")
def metrics():
    """Prometheus scrape endpoint."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
