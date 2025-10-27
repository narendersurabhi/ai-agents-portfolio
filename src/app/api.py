from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.orchestration_agent import OrchestrationAgent

app = FastAPI()
agent = OrchestrationAgent()

class AskIn(BaseModel):
    question: str

@app.post("/ask")
def ask(body: AskIn):
    return agent.run(body.question)
