from pydantic import BaseModel
import json


# Task 1:Multiple AgentConfiguration Logger
# -----------------------------------------------


# create pydantic Base Model
class AgentiConfig(BaseModel):
    agent_id:int
    agent_name:str
    role:str

# ---  CREATE SAMPLE DATA ---
agents_raw_data = [
    {"agent_id": 101, "agent_name": "Hari", "role": "Automation"},
    {"agent_id": 102, "agent_name": "Joseph", "role": "Research"},
    {"agent_id": 103, "agent_name": "Charley", "role": "UI Design"}
]

# Create empty list for store datas
validated_agents_list = []

for items in agents_raw_data:
    try:
        # validated each data
        validated_data = AgentiConfig(**items)
        # create dictionary of data
        dict_data = validated_data.model_dump()
        # append data to empty list
        validated_agents_list.append(dict_data)
    except Exception as e:
         print(f"[ERROR] Validation failed for an agent: {e}")

agent_file = "multiple_agents.json"

with open(agent_file, "w")as file:
    json.dump(validated_agents_list, file,indent=4)

with open(agent_file, "r")as file:
    loaded_data = json.load(file)
print("Loading International AI Fleet")    
print("=============================================")
#  data take each list

for agent in loaded_data:
    print(f"Agent id :{agent["agent_id"]}\nAgent_name :{agent["agent_name"]}\nAgent Role:{agent["role"]}\n")    
    print("============================================")















