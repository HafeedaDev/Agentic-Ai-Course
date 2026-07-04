
import json
from pydantic import BaseModel

# # step 1:create pydantic model

class AgentFilterModel(BaseModel):
     agent_id: int
     agent_name: str
     status: str
     accuracy: int

# # Step 2: Raw Input data

agent_pool_raw = [
     {"agent_id": 101, "agent_name": "Jarvis", "status": "active", "accuracy": 95},
     {"agent_id": 102, "agent_name": "Ultron", "status": "inactive", "accuracy": 88},
     {"agent_id": 103, "agent_name": "Friday", "status": "active", "accuracy": 92},
     {"agent_id": 104, "agent_name": "Saiyaara", "status": "inactive", "accuracy": 96},
     {"agent_id": 105, "agent_name": "Eko", "status": "active", "accuracy": 89}
]    

# # create empty list
active_agents_list = []

print("Filtering active agents from pool...")

# # step 3: Loop Validate & Filter Logic

for agents in agent_pool_raw:
    try:
        # vlidation through pydantic
        validated_data = AgentFilterModel(**agents)
        # filter active agent with condition
        if validated_data.status == "active":
            active_agents_list.append(validated_data.model_dump())
    except Exception as e:
        print("Validation failed  for an agent: {e}")

# # Step 4: convert active agents to json file
file_name = "active_agents_fleet.json"
print(f"Saving  active fleet to {file_name}...\n")

with open(file_name, "w") as file:
    json.dump(active_agents_list, file, indent=4)

# # Step 5:  load the file print in Terminal
with open(file_name, "r") as file:
    loaded_file = json.load(file)
    print("Deploying Active AI AGENT FLEET....")
    print("=" * 50)
for agent in loaded_file:
    print(f"Agent Name: {agent['agent_name']}\nAccuracy: {agent['accuracy']}%\n")
    print("-" * 50)
print("=" * 50)        
  
  # -------------------------------------------------------------
 