from app.core.llm import llm
from langchain_core.prompts import PromptTemplate
import json

entity_prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an information extraction agent.

Extract entities from the message.

Possible entities:
- order_id
- amount
- date
- property_id
- flat_number

Rules:
- Return ONLY valid JSON
- If an entity is not found, return null for that field

Message:
{message}
"""
)

def extract_entities(message: str) -> dict:
    chain = entity_prompt | llm
    response = chain.invoke({"message": message})

    raw_output = response.content.strip()

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        # Safe fallback to avoid 500 Internal Server Error
        return {
            "order_id": None,
            "amount": None,
            "date": None,
            "property_id": None,
            "flat_number": None
        }
