from backend.agent.agent import run_agent
import json

if __name__ == "__main__":
    scenario = "Iran stops oil exports to India"

    result = run_agent(scenario)

    print(json.dumps(result, indent=2))