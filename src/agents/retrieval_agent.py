from src.tools.vector_store import LocalVectorStore

class RetrievalAgent:
    def __init__(self, top_k=4):
        self.vs = LocalVectorStore("data/vector_index")

    def run(self, question: str):
        docs = self.vs.search(question, top_k=4)
        # call LLM with retrieved context (pseudo)
        answer = {
            "answer": f"Grounded answer to: {question}",
            "sources": [d["id"] for d in docs],
        }
        return answer
