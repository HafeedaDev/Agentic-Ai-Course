import json
from pydantic import BaseModel

#  Step 1: AI Agent Task Allocator Logger
class AgentAllocatorLogger(BaseModel):
      task_id : int
      agent_name:str
      assigned_job:str

# step 2: Sample data

allocated_tasks_raw = [
    {"task_id": 501, "agent_name": "Jarvis", "assigned_job": "Database Backup"},
    {"task_id":" abc", "agent_name": "Saiyaara", "assigned_job": "Market Trend Analysis"},
    {"task_id": 503, "agent_name": "Friday", "assigned_job": "UI Layout Redesign"}
]

validated_agent_list = []

print(f" Saving validated tasks to agent_tasks_output.json...") 

# strp 3: Iterate datas from loop
for datas in allocated_tasks_raw:
    try:  
        validated_data = AgentAllocatorLogger(**datas)
        dict_data = validated_data.model_dump()
        validated_agent_list.append(dict_data)
    except Exception as e:
           print(f"⚠️ Validation failed for an agent: {e}")
        

file_name = "agent_allocated_tasks.json"        

with open(file_name, "w")as file:
    json.dump(validated_agent_list, file,indent=4)
    print(f"[SUCCESS] All tasks allocated and logged successfully.") 

with open(file_name ,"r")as file:
      loaded_data = json.load(file)
      print(" LOADING CURRENT TASK ALLOCATIONS...")   
      print("====================================")
      
for item in loaded_data:
    print(f"Agent Id:{item["task_id"]}\nAgent Name:{item["agent_name"]}\nAgent Job:{item["assigned_job"]}")     
    print("====================================")       

