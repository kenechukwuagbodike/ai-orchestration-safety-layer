import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

# Initialize app
app = FastAPI(
    title="AI Orchestration & Safety Layer",
    description="An API for safe GenAI Orchestration with guardrails and monitoring.",
    version="0.1.0"
)

# API key (default = dev key if env is not set)
API_KEY = os.getenv("API_KEY", "dev_key")

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
    # Auth check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    #For now, just echo back the prompt
    return {
        "status": "ok",
        "user": q.user_id,
        "response": f"Echo: {q.prompt}"
    }
