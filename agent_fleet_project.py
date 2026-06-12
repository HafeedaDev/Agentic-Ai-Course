import json
from pydantic import BaseModel

# --- STEP 1: DEFINE PYDANTIC SCHEMA FOR DATA VALIDATION ---
class AgentConfig(BaseModel):
    agent_id: int
    agent_name: str
    role: str
    is_active: bool
    max_iterations: int

# --- STEP 2: CREATE SAMPLE DATA ---
config_data = {
    "agent_id": 201,
    "agent_name": "Saiyaara",
    "role": "Research Specialist",  
    "is_active": True,
    "max_iterations": 5
}

# Validating data through the Pydantic model
config_agent_data = AgentConfig(**config_data)

# --- STEP 3: CONVERT TO DICTIONARY AND SAVE TO JSON ---
json_file = "agent_fleet.json"  

print("Saving validated configuration to JSON file...")


# Converting Pydantic object to a standard Python dict before dumping
agent_dict = config_agent_data.model_dump()

with open(json_file, "w") as file:
    json.dump(agent_dict, file, indent=4)  

print("[SUCCESS] Data successfully saved.")  


# --- STEP 4: LOAD AND DISPLAY DATA FROM JSON ---
print("\n Loading data back from JSON file...")

with open(json_file, "r") as file:
    loaded_data = json.load(file)

# Professional multi-line output using single print and \n
print(f"\n AI AGENT FLEET MANAGEMENT SYSTEM\n======================\n Agent ID    : {loaded_data['agent_id']}\n Agent Name  : {loaded_data['agent_name']}\n System Role  : {loaded_data['role']}\n Max Loops   : {loaded_data['max_iterations']}\n Fleet Status : {'Active' if loaded_data['is_active'] else 'Inactive'}\n======================")