from src.agents.retrieval_agent import RetrievalAgent
from src.agents.tooluse_agent import ToolUseAgent

class OrchestrationAgent:
    def __init__(self):
        self.retrieval = RetrievalAgent()
        self.tools = ToolUseAgent()

    def run(self, question: str):
        if any(k in question.lower() for k in ["summarize","explain","what is"]):
            return {"route":"retrieval","result": self.retrieval.run(question)}
        if question.lower().startswith("tool:"):
            return {"route":"tooluse","result": self.tools.run(question[5:])}
        return {"route":"fallback","result": {"answer":"Try 'summarize ...' or 'tool: search: <q>'"}}

