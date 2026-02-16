from app.core.llm import llm

print(llm.invoke("Say hello in one short sentence").content)
