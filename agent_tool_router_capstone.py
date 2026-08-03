
from pydantic import BaseModel

# 1. Inner Model (Tool details)
class ToolSpec(BaseModel):
    tool_name: str
    is_enabled: bool

# 2. Outer Model (Agent Routing Details)
class AgentRouter(BaseModel):
    agent_id: str
    role: str
    primary_tool: ToolSpec  # Nested Model!

# 3. Incoming Multi-Agent Payload
raw_payload = [
    {
        "agent_id": "AGT-01",
        "role": "search_agent",
        "primary_tool": {"tool_name": "google_search", "is_enabled": True}
    },
    {
        "agent_id": "AGT-02",
        "role": "coder_agent",
        "primary_tool": {"tool_name": "python_interpreter", "is_enabled": False}
    },
    {
        "agent_id": "AGT-03",
        "role": "sql_agent",
        "primary_tool": {"tool_name": "db_query_tool", "is_enabled": True}
    }
]
# 4. Dictionary Comprehension + Nested Pydantic Validation:
active_tool_map = {
    item["agent_id"]:AgentRouter(**item)
    for item in raw_payload
    if item["primary_tool"]["is_enabled"] == True
    
}

print(f"count :{len(active_tool_map)}")

for id_item, obj_item in active_tool_map.items():
 print(f"{id_item} | role:{obj_item.role}| ToolName:{obj_item.primary_tool.tool_name}")


