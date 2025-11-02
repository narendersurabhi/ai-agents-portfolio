import argparse, json, os
from dotenv import load_dotenv
from src.agents.orchestration_agent import OrchestrationAgent

def main():
    # Load environment variables from .env if present, overriding existing
    # env to avoid stale keys in the shell.
    load_dotenv(override=True)
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["ask"])
    p.add_argument("query")
    p.add_argument("--top-k", type=int, default=4, dest="top_k", help="Top-k chunks to use")
    p.add_argument("--model", default=os.getenv("CHAT_MODEL") or "gpt-4o-mini", help="Model for retrieval synthesis (CLI only)")
    p.add_argument("--markdown", action="store_true", help="Print markdown instead of JSON")
    args = p.parse_args()

    agent = OrchestrationAgent()
    # Adjust retrieval settings for CLI
    try:
        agent.retrieval.top_k = int(args.top_k)
    except Exception:
        pass
    try:
        agent.retrieval.model = str(args.model)
    except Exception:
        pass
    out = agent.run(args.query)

    if args.markdown and isinstance(out, dict) and out.get("route") == "retrieval":
        res = out.get("result", {}) or {}
        answer = res.get("answer", "")
        sources = res.get("sources", []) or []
        lines = []
        lines.append(answer)
        if sources:
            lines.append("\nSources:")
            for i, s in enumerate(sources, start=1):
                lines.append(f"- [{i}] {s}")
        print("\n".join(lines))
    else:
        print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
