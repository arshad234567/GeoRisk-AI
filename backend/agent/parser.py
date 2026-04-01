def parse_tool_call(response: str):
    if "TOOL_CALL" not in response:
        return None, None

    try:
        _, tool_data = response.split("TOOL_CALL:")
        tool_name, tool_input = tool_data.split(":", 1)

        return tool_name.strip(), tool_input.strip()
    except:
        return None, None