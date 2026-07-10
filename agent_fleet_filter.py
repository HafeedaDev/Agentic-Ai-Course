
from pydantic import BaseModel, RootModel, ValidationError
from typing import List 

# step 1: PYDANTIC MODEL DEFINITION
# -----------------------------------------
class AiAgent(BaseModel):
    # validate single agent data BaseModel
    agent_id: int 
    agent_name: str 
    status: str
    max_loops: int

#  All list validate using RootModel

class AiAgentList(RootModel[List[AiAgent]]):
    pass

# Step 2:PROFESSIONAL PRINT FUNCTION (Type Hinting)
# ---------------------------------------------------
def print_active_agents(active_list: List[AiAgent]):
    # A function to print only active agents in a prefessional manner
    print("="*50)
    print("ACTIVE AGENTS FLEET")
    print("="*50)

    if not active_list:
        print("No Active agents found ")
    else:
        for agent in active_list:
            # It is a Pydantic Object,get values directly by putting a dot (.)
            print(f"ID:{agent.agent_id} | Name:{agent.agent_name:<10} | Max Loops: {agent.max_loops} ")
    print("="*50)

# step 3: RAW DATA & MAIN LOGIC (Try-Execept)
                
raw_fleet_data = [
    {"agent_id": 101, "agent_name": "Alpha", "status": "active", "max_loops": 5},
    {"agent_id": 102, "agent_name": "Beta", "status": "inactive", "max_loops": 3},
    {"agent_id": 103, "agent_name": "Gamma", "status": "active", "max_loops": 7},
    {"agent_id": 104, "agent_name": "Delta", "status": "busy", "max_loops": 4},
    {"agent_id": 105, "agent_name": "Epsilon", "status": "active", "max_loops": 6}
]
try:
    # all list validate using pydantic
    validated_fleet = AiAgentList.model_validate(raw_fleet_data)

    # '.root'is used to retrive the actual list from 'RootModel'
    actual_agent_list = validated_fleet.root

    # Filtering only "active" agencise using list Comprehention
    active_agents_only = [agent for agent in actual_agent_list if agent.status =="active"]

    # The filtered list is passed to the function printing
    print_active_agents(active_agents_only)

except ValidationError as e:
    print(f"pydantic validation is fail {e}")
except Exception as e:
    print(f"Error {e}")    

