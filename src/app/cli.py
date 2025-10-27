import argparse, json, os
from src.agents.orchestration_agent import OrchestrationAgent

def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["ask"])
    p.add_argument("query")
    args = p.parse_args()

    agent = OrchestrationAgent()
    out = agent.run(args.query)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
