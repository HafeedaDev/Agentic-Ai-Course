
from pydantic import BaseModel

#1 Inner  Model
class ModelConfig(BaseModel):
    temperature: float
    model_name: str

#2 Outer Model    
class AgentSystem(BaseModel):
    system_id: str
    status: str
    config: ModelConfig #inner model using here

#3 Incoming API Stream (Nested Dictionary List)    
raw_system_stream = [
    {
        "system_id": "SYS-ALPHA",
        "status": "ready",
        "config": {"temperature": 0.2, "model_name": "gpt-4o"}
    },
    {
        "system_id": "SYS-BETA",
        "status": "busy",
        "config": {"temperature": 0.7, "model_name": "claude-3-5-sonnet"}
    },
    {
        "system_id": "SYS-GAMMA",
        "status": "ready",
        "config": {"temperature": 0.0, "model_name": "gpt-4o-mini"}
    }
]

# 4 Dictionary Comprehension  + Nested Pydantic Validation

ready_system_map = {
    sys["system_id"]:AgentSystem(**sys)
    for sys in raw_system_stream 
    if sys["status"] == "ready"
}

# 5 Deep Extraction &Output check 
print("="*50)
# print(f"Ready System Count:{len(ready_system_map)}")
# print(f"SYS_ALPHA Temperature: {ready_system_map['SYS-ALPHA'].config.temperature}")
# print(f"SYS-ALPHA Model: {ready_system_map['SYS-ALPHA'].config.model_name}")


for sys_id, sys_obj in ready_system_map.items():
    print(f"{sys_id} Model: {sys_obj.config.model_name} | Temp: {sys_obj.config.temperature}")

    print("="*50)