from app.core.llm import llm
from langchain_core.prompts import PromptTemplate

urgency_prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an AI classifier.

Classify the urgency strictly as ONE of:
Low
Medium
High
Critical

Rules:
- Return ONLY one word
- No punctuation
- No explanation

Critical means: fraud, money loss, safety risk, or legal threat.

Message:
{message}
"""
)

def classify_urgency(message: str) -> str:
    chain = urgency_prompt | llm
    response = chain.invoke({"message": message})
    return response.content.strip()
