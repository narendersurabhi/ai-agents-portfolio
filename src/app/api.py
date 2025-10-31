from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.orchestration_agent import OrchestrationAgent

app = FastAPI(title="AI Agents")
agent = OrchestrationAgent()

class AskIn(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "ok", "service": "ai-agents-portfolio"}

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/ask")
def ask(body: AskIn):
    return agent.run(body.question)
