import os, glob
class LocalVectorStore:
    def __init__(self, path): self.path = path
    def search(self, query, top_k=4):
        # placeholder logic; swap with faiss index
        hits = [{"id": p, "score": 1.0} for p in sorted(glob.glob("data/docs/*"))][:top_k]
        return hits
