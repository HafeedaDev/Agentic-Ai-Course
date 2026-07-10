from pydantic import BaseModel, RootModel, ValidationError
from typing import  List

# Step 1: Pydentic Model Definition
class AgentLoadModel(BaseModel):
    agent_id: int
    agent_name: str
    role: str
    current_tasks: int

# All list validate using RootModel
class AgentLoadList(RootModel[List[AgentLoadModel]]):
    pass

# Step 2:Create Function
def print_high_load_agents(active_list: List):
    print("="*50)
    print("HIGH LOAD AGENTS ALERT")
    print("="*50)

    if not active_list:
        print("Not found data")
    else:
        for agent in active_list:
         print(f"ID: {agent.agent_id} Name: {agent.agent_name:<10} Role: {agent.role} Tasks:{agent.current_tasks}") 

# Raw Data      
    
agent_load_raw = [
    {"agent_id": 201, "agent_name": "Lex", "role": "Scraper", "current_tasks": 3},
    {"agent_id": 202, "agent_name": "Max", "role": "Analyzer", "current_tasks": 6},
    {"agent_id": 203, "agent_name": "Neo", "role": "Coder", "current_tasks": 8},
    {"agent_id": 204, "agent_name": "Rex", "role": "Tester", "current_tasks": 2},
    {"agent_id": 205, "agent_name": "Zox", "role": "Writer", "current_tasks": 5}
]
    
try:
    # All list validate using RootModel
    validate_agent_list = AgentLoadList.model_validate(agent_load_raw) 
    # '.root'is used to retrive the actual list from 'RootModel'
    actual_agent_fleet = validate_agent_list.root
    # Filtering only "active" agencise using list Comprehention
    high_load_agents = [agent for agent in actual_agent_fleet if agent.current_tasks >=5]
    # The filtered list is passed to the function printing
    print_high_load_agents(high_load_agents)

except ValidationError as e:
    print(f"Pydantic validation is fail {e}")   
except Exception as e:
    print("found error{e}")
