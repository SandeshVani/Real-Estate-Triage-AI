from crewai import Crew, Agent, Task
from app.agents.intent_agent import classify_intent
from app.agents.urgency_agent import classify_urgency
from app.agents.entity_agent import extract_entities
from app.agents.response_agent import draft_response

def run_triage(message: str):
    intent = classify_intent(message)
    urgency = classify_urgency(message)
    entities = extract_entities(message)
    response = draft_response(intent, urgency, message)

    return {
        "intent": intent,
        "urgency": urgency,
        "entities": entities,
        "draft_response": response
    }
