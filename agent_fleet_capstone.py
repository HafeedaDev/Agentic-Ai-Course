
from pydantic import BaseModel, Field, RootModel, ValidationError
from typing import List

# Mini Project including python TypeHinting,Data Classes ,Pydantic data validation ,List Comprehension,filter() + lambda
#------------------------------------------------------------------------------------------------------------------------

# Step 1: Create Pydantic Model

class AIAgent(BaseModel):
    agent_id: str
    agent_name: str
    active_tasks: int
    status: str
    memory_usage_mb: float = Field(gt=0) #Myst be strictly > 0

class AIAgentList(RootModel[List[AIAgent]]):
    pass

print("="*50)
print("Phase 1 Consolidation Project: Agent Fleet Traffic Manager")
print("="*50)

# Step 2: Create Function 

def process_fleet_data(fleet_data: List[AIAgent]):
    if not fleet_data:
        print("Not fount data")
    else:
        for agent in fleet_data:
            print(f"ID: {agent.agent_id} | Name: {agent.agent_name} | Task: {agent.active_tasks}| Status: {agent.status} | Memory_usage_mb: {agent.memory_usage_mb}")

# Create Data
raw_fleet_data = [
    {
        "agent_id": "AGENT-001",
        "agent_name": "alpha-processor",
        "active_tasks": 3,
        "status": "active",
        "memory_usage_mb": 256.5
    },
    {
        "agent_id": "AGENT-002",
        "agent_name": "beta-worker",
        "active_tasks": 0,
        "status": "idle",
        "memory_usage_mb": 328.0
    },
    {
        "agent_id": "AGENT-003",
        "agent_name": "gamma-analyzer",
        "active_tasks": 5,
        "status": "active",
        "memory_usage_mb": 250.0
    },
    {
        "agent_id": "AGENT-004",
        "agent_name": "delta-router",
        "active_tasks": 2,
        "status": "offline",
        "memory_usage_mb": 64.0
    },
    {
        "agent_id": "AGENT-005",
        "agent_name": "epsilon-monitor",
        "active_tasks": 4,
        "status": "RUNNING", 
        "memory_usage_mb": 512.0
    },
    {
        "agent_id": "AGENT-006",
        "agent_name": "zeta-executor",
        "active_tasks": 8,
        "status": "active",
        "memory_usage_mb": 1024.0
    }
]

# Step 3: Validation with Try - Exception
try:
    validate_fleet_data = AIAgentList.model_validate(raw_fleet_data)
    validated_data = validate_fleet_data.root
    data_comprehension = [
        AIAgent(
            agent_id = agent.agent_id,
            agent_name = agent.agent_name.upper(),
            active_tasks = agent.active_tasks,
            status = agent.status,
            memory_usage_mb = agent.memory_usage_mb
        )
        for agent in validated_data
    ]
    filtered_data = filter(lambda emp : emp.status in ['active' ,'idle' ,'offline'] and emp.memory_usage_mb >200 ,data_comprehension)
    filterd_data_agent = list(filtered_data)
    process_fleet_data(filterd_data_agent)

except ValidationError as e:
    print(f"Got validation error {e}")  
except Exception as e :
    print(f"Got Error {e}")

  