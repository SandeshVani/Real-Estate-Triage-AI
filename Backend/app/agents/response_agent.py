from app.core.llm import llm
from langchain_core.prompts import PromptTemplate

response_prompt = PromptTemplate(
    input_variables=["intent", "urgency", "message"],
    template="""
You are a professional customer support assistant.

Context:
- Intent: {intent}
- Urgency: {urgency}

Customer message:
{message}

Write a short, polite, clear, and reassuring response.
Do NOT use markdown.
Do NOT add greetings like "Dear Customer".
Do NOT sign off with a name.
"""
)

def draft_response(intent: str, urgency: str, message: str) -> str:
    chain = response_prompt | llm
    response = chain.invoke({
        "intent": intent,
        "urgency": urgency,
        "message": message
    })
    return response.content.strip()
