import os
from fastapi import FastAPI, Header, HTTPException, Response
from pydantic import BaseModel

from app.moderation import is_safe
from app.logger import write_audit_log # <-- NEW
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# Initialize app
app = FastAPI(
    title="AI Orchestration & Safety Layer",
    description="An API for safe GenAI Orchestration with guardrails and monitoring.",
    version="0.1.0"
)

# API key (default = dev key if env is not set)
API_KEY = os.getenv("API_KEY", "dev_key")

# Prometheus Metrics
REQUESTS_TOTAL = Counter('requests_total', 'Total number of requests')
BLOCKED_TOTAL = Counter('blocked_requests_total', 'Total number of blocked requests')

# Define input schema
class Query(BaseModel):
    user_id: str
    prompt: str
    
# Root Health Check
@app.get("/")
async def root():
    return {"status": "ok", "message": "AI Orchestration API is running."}

# Core Orchestration Endpoint
@app.post("/v1/query")
async def query(q: Query, x_api_key: str = Header(None)):
    REQUESTS_TOTAL.inc() # Increment request count
    write_audit_log(q.user_id, q.prompt, "received") # Log received request
    
    # Check API Key
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    # Run Moderation Check
    safe, reason = is_safe(q.prompt)
    if not safe:
        BLOCKED_TOTAL.inc() # Increment blocked count
        write_audit_log(q.user_id, q.prompt, "blocked", reason)
        return {
            "status": "blocked",
            "user_id": q.user_id,
            "reason": reason
        }
        
    # If safe, return echo response (placeholder for actual orchestration logic)
    return {
        "status": "ok",
        "user_id": q.user_id,
        "response": f"Echo: {q.prompt}"
    }
    
# Prometheus Metrics Endpoint
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)