from src.tools.web_search import web_search
from src.tools.s3_client import safe_put_object

class ToolUseAgent:
    def run(self, task: str):
        if "search" in task.lower():
            q = task.split(":",1)[-1].strip()
            return {"tool":"web_search","data": web_search(q)}
        if "store" in task.lower():
            return safe_put_object("ai-agents-demo", "note.txt", b"demo")
        return {"message": "no-op"}
