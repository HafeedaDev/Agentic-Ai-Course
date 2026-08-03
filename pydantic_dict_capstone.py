
# pydantic validation with Dictionary comprehension

from pydantic import BaseModel
# Agent Pydantic Model

class AgentMetricModel(BaseModel):
    agent_id: str
    name: str
    tasks_completed: int
    region: str
    is_active: bool

# Raw JSON/Dict List from API
agent_metrics = [
    {"agent_id": "A-101", "name": "vector_processor", "tasks_completed": 120, "region": "US-East", "is_active": True},
    {"agent_id": "A-102", "name": "prompt_evaluator", "tasks_completed": 45, "region": "EU-West", "is_active": False},
    {"agent_id": "A-103", "name": "rag_retriever", "tasks_completed": 310, "region": "US-East", "is_active": True},
    {"agent_id": "A-104", "name": "tool_router", "tasks_completed": 88, "region": "AP-South", "is_active": True},
]
# pydantic validation and dictionary comprehension
# key -> agent_id
# value -> Validated pydantic object

agent_pydantic_map = {
    agent["agent_id"]: AgentMetricModel(**agent)
    for agent in agent_metrics 
    if agent["is_active"]
}

# print(agent_pydantic_map)

#Fast &safe Access (Dot Notation +Dict Lookup)
print(agent_pydantic_map["A-101"])
print(agent_pydantic_map["A-103"])