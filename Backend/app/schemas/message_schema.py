from pydantic import BaseModel

class MessageInput(BaseModel):
    source: str
    raw_text: str
