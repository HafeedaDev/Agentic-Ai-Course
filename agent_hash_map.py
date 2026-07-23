from pydantic import BaseModel

# 1. Agent Pydantic Model
class AgentModel(BaseModel):
    agent_id: str
    name: str
    workload: int
    is_active: bool

# Raw JSON/Dict List from API
raw_agent_stream = [
    {"agent_id": "SYS-01", "name": "router_agent", "workload": 15, "is_active": True},
    {"agent_id": "SYS-02", "name": "cleaner_agent", "workload": 95, "is_active": False},
    {"agent_id": "SYS-03", "name": "analyzer_agent", "workload": 60, "is_active": True},
    {"agent_id": "SYS-04", "name": "deployer_agent", "workload": 40, "is_active": True},
]

active_agent_registry = {
    agent["agent_id"]: AgentModel(**agent)
    for agent in raw_agent_stream if agent["is_active"]
}
print(f"Registered Agents Count:{len(active_agent_registry)}")
print(f"Agent SYS-03 Name:{active_agent_registry["SYS-03"].name.upper()}")
print(f"Agent SYS-03 Workload:{active_agent_registry['SYS-03'].workload}")