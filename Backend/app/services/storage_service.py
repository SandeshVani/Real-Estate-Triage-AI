import uuid
from datetime import datetime

def store_message(message, triage_result):
    return {
        "ticket_id": str(uuid.uuid4()),
        "message": message,
        "triage": triage_result,
        "created_at": datetime.utcnow()
    }
