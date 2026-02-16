from langchain_core.prompts import PromptTemplate
from app.core.llm import llm

prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are a Support Triage AI.

Classify the intent into ONE of the following:
- BUY
- SELL
- RENT
- SUPPORT
- GENERAL

Rules:
- Return ONLY one word
- No explanation
- No punctuation

User message:
{message}
"""
)

def classify_intent(message: str) -> str:
    chain = prompt | llm
    response = chain.invoke({"message": message})
    return response.content.strip().upper()
