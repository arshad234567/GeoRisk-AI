def get_india_context(query: str):
    return "India imports around 80% of its crude oil."

def calculate_impact(data: str):
    return "Estimated inflation may increase by 2%."

TOOLS = {
    "get_india_context": get_india_context,
    "calculate_impact": calculate_impact,
}