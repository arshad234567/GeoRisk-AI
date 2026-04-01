import json
from backend.agent.prompt import SYSTEM_PROMPT
from backend.agent.llm import call_llm
from backend.agent.parser import parse_tool_call
from backend.agent.config import MAX_STEPS
from backend.tools.registry import TOOLS

def run_agent(user_input: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    for step in range(MAX_STEPS):
        response = call_llm(messages)

        # Try final JSON output
        try:
            return json.loads(response)
        except:
            pass

        # Check for tool call
        tool_name, tool_input = parse_tool_call(response)

        if tool_name and tool_name in TOOLS:
            tool_result = TOOLS[tool_name](tool_input)

            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "tool", "content": tool_result})

            continue

        # fallback
        return {"raw": response}

    return {"error": "Max steps reached"}