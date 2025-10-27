from src.agents.orchestration_agent import OrchestrationAgent

def test_routes():
    a = OrchestrationAgent()
    assert a.run("summarize the docs")["route"] == "retrieval"
    assert a.run("tool: search: ai news")["route"] == "tooluse"
