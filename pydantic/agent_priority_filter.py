
import json
from pydantic import BaseModel


class AgentPriorityFilter(BaseModel):
    agent_id: int
    agent_name: str
    priority: str
    version: float

# raw data
agent_priority_raw = [
    {"agent_id": 401, "agent_name": "Jarvis", "priority": "High", "version": 2.5},
    {"agent_id": 402, "agent_name": "Friday", "priority": "Medium", "version": 1.8},
    {"agent_id": 403, "agent_name": "Ultron", "priority": "High", "version": 3.0},
    {"agent_id": 404, "agent_name": "Saiyaara", "priority": "Low", "version": 1.2},
    {"agent_id": 405, "agent_name": "Eko", "priority": "High", "version": 2.0}
]

# create empty list
high_priority_list = []

# validation throuh pydantic
for agent in agent_priority_raw:
    try:
        priority_data = AgentPriorityFilter(**agent)
        if priority_data.priority == "High":
          high_priority_list.append(priority_data.model_dump())    
    except Exception as e:
        print("Validation failed  for an agent: {e}")    


 # Step 4: convert allocation list  to json file
file_name = 'high_priority_filter.json' 

with open(file_name, "w")as file:
    json.dump(high_priority_list, file, indent=4)

with open(file_name, "r")as file:
    loaded_data = json.load(file)
   
for item in loaded_data:
     print(f"Agent Name:{item['agent_name']} \n priority:{item['priority']}")
     print("-"*10)  