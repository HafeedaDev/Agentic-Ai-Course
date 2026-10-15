from pydantic import BaseModel ,RootModel ,ValidationError
from typing import List

# step1: Pydantic Model Definition

class AgentModel(BaseModel):
    agent_id: int
    agent_name: str
    status: str
    accuracy: int

# All list validate using RootModel
class AgentPoolList(RootModel[List[AgentModel]]):
    pass




# Step 2: Create Function
def print_elite_agents(elite_list:List):
    print("="*50)
    print("ELITE ACTIVE AGENTS (>90% ACCURACY)")
    print("="*50)

    if  not elite_list:
        print("Not Fount Data")
    else:
        for item in elite_list:
         print(f"ID: {item.agent_id} Name: {item.agent_name:<10} Accuracy:{item.accuracy}")    
    print("="*50)

# step 3: RAW DATA & MAIN LOGIC (Try-Execept)
agent_pool_raw = [
     {"agent_id": 101, "agent_name": "Jarvis", "status": "active", "accuracy": 95},
     {"agent_id": 102, "agent_name": "Ultron", "status": "inactive", "accuracy": 88},
     {"agent_id": 103, "agent_name": "Friday", "status": "active", "accuracy": 92},
     {"agent_id": 104, "agent_name": "Saiyaara", "status": "inactive", "accuracy": 96},
     {"agent_id": 105, "agent_name": "Eko", "status": "active", "accuracy": 89}
]

try:
   # all list validate using pydantic 
    validate_elite_list = AgentPoolList.model_validate(agent_pool_raw)

   # retrive actual list from RootModel
    actual_agent_list = validate_elite_list.root

    # Filtering only "active" agencise using list Comprehention
    active_agents_only = [agent for agent in actual_agent_list if agent.status == 'active' and agent.accuracy >90]

    print_elite_agents(active_agents_only)
    # The filtered list is passed to the function printing
except ValidationError as e:
    print(f"pydantic validation is fail {e}")
except Exception as e:
    print(f"Error {e}")   