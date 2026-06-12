from pydantic import BaseModel
import json

# --- STEP 1: DEFINE PYDANTIC SCHEMA FOR DATA VALIDATION ---
class InternationalAgent(BaseModel):
    agent_id:int
    agent_name:str
    target_market:str
    hourly_rate:float
    is_verified:bool

# --- STEP 2: CREATE SAMPLE DATA --- 
raw_agent_data = {
    "agent_id": 5001,
    "agent_name": "Saiyaara-Remote",
    "target_market": "Global International",
    "hourly_rate": 75.00,
    "is_verified": True
}
# Validating data through the Pydantic model

agent_data = InternationalAgent(**raw_agent_data)

# --- STEP 3: CONVERT TO DICTIONARY AND SAVE TO JSON ---

agent_file = "international_agent_data.txt"

# Converting Pydantic object to a standard Python dict before dumping

dict_data = agent_data.model_dump()
\

with open(agent_file, "w")as file:
    json.dump(dict_data, file,indent=4)
print(f"[SUCCESS] Agent data saved to Hard Disk")    


# --- STEP 4: LOAD AND DISPLAY DATA FROM JSON ---
with open(agent_file, "r")as file:

    loaded_data = json.load(file)
print(f"\n----------------------\n Agent Id : {loaded_data[ "agent_id"]}\n Agent Name:{loaded_data["agent_name"]}\n Target Market: {loaded_data[  "target_market"]} \n Hourly Rate: {loaded_data[  "hourly_rate"]}\n Is Verified : {loaded_data["is_verified"]}\n --------------------- ")    



