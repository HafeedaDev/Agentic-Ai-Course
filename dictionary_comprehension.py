
# Dictionary Comprehension 

raw_agents = [
    {"id": "A-1", "name": "data_extractor", "workload_score": 85, "active": True},
    {"id": "A-2", "name": "log_analyzer", "workload_score": 40, "active": False},
    {"id": "A-3", "name": "model_deployer", "workload_score": 92, "active": True},
    {"id": "A-4", "name": "cache_cleaner", "workload_score": 15, "active": True},
]

raw_data_comprehension = {
    agent["id"]:agent["name"].upper() for agent in raw_agents  if agent["active"]== True and agent["workload_score"]> 50
} 
print(raw_data_comprehension)


agent_metrics = [
    {"agent_id": "A-101", "name": "vector_processor", "tasks_completed": 120, "region": "US-East", "is_active": True},
    {"agent_id": "A-102", "name": "prompt_evaluator", "tasks_completed": 45, "region": "EU-West", "is_active": False},
    {"agent_id": "A-103", "name": "rag_retriever", "tasks_completed": 310, "region": "US-East", "is_active": True},
    {"agent_id": "A-104", "name": "tool_router", "tasks_completed": 88, "region": "AP-South", "is_active": True},
]

active_agent_summery = {
    agent["agent_id"]:(agent["name"],agent["region"]) for  agent in agent_metrics if agent["is_active"] == True
}
print(f"Active Agent Summery :{active_agent_summery}")

high_performer_map = {
   agent["name"].upper():agent["tasks_completed"]
    for agent in agent_metrics if agent["tasks_completed"]>100
}
print(f"High Performer Map:{high_performer_map}")