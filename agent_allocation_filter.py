import json
from pydantic import BaseModel


# step 1:Create pydantic model

class AgentAllocationModel(BaseModel):
    agent_id :int
    agent_name:str
    allocation_status:str
    priority:str

# Sample data

agent_allocation_raw = [
    {"agent_id": 301, "agent_name": "Jarvis", "allocation_status": "allocated", "priority": "High"},
    {"agent_id": 302, "agent_name": "Friday", "allocation_status": "allocated", "priority": "Medium"},
    {"agent_id": 303, "agent_name": "Saiyaara", "allocation_status": "unallocated", "priority": "None"},
    {"agent_id": 304, "agent_name": "Eko", "allocation_status": "allocated", "priority": "Low"},
    {"agent_id": 305, "agent_name": "Ultron", "allocation_status": "unallocated", "priority": "None"}
]

# create empty list
allocated_list = []
print("Filtering active agents from pool...")

# step 3: Loop Validate & Filter Logic
for agent in agent_allocation_raw:
    try:
        agent_allocation_data = AgentAllocationModel(**agent)
        if agent_allocation_data.allocation_status == "allocated":
           allocated_list.append(agent_allocation_data.model_dump())
    except Exception as e:
        print("Validation failed  for an agent: {e}")       

 # Step 4: convert allocation list  to json file
file_name =  "allocated_agents.json" 

with open(file_name, "w")as file:
    json.dump(allocated_list,file,indent=4)

with open(file_name, "r")as file:
    loaded_data = json.load(file)
    print("-"*10)

for item in loaded_data:
    print(f"Agent ID:{item['agent_id']} Agent Name:{item['agent_name']} Allocation Status:{item['allocation_status']} ")
    
    print("-"*10)

