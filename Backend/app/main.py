from fastapi import FastAPI
from pydantic import BaseModel
from app.services.triage_service import triage_message

app = FastAPI()

class TriageRequest(BaseModel):
    raw_text: str

class TriageResponse(BaseModel):
    intent: str
    urgency: str
    entities: dict
    response: str

@app.post("/triage", response_model=TriageResponse)
def triage_endpoint(payload: TriageRequest):
    result = triage_message(payload.raw_text)
    return result
