
import json

# Task1:
# dictionary data convert json file
# Part 1: Write/Dump
  
agent_settings = {
    "agent_name" :"Jarvis",
    "role": "AI System Designer",
    "status": "Active"
} 
json_file_name = "agent_config.json"

print("Saving agent settings  to JSON file...")
with open(json_file_name, "w")as file:
    json.dump(agent_settings, file, indent=4)
print("[WRITE SUCCESS] JSON file has been created")    

# ---Part 2:Reading Data Back From Json File---

print("\n Reading data  back from JSON File..")
with open(json_file_name, "r") as file:
    loaded_data = json.load(file)
print(f"[Load Success] Agent name is: {loaded_data["agent_name"]}")
print(f" Agent Role is:{loaded_data['role']}")
print(f"Status:{loaded_data['status']}")


# Task2: AI Agent Metrics Tracker

agent_data = {
    "total_tasks": 50,
    "success_rate":"96%",
    "execution_time":"4-5 seconds"
}

agent_json_file = "agent_metrics.json"

with open(agent_json_file, "w")as file:
    json.dump(agent_data, file,indent=4)
print("[Success] Json file has been created")

with open(agent_json_file, "r")as file:
   loaded_datas =  json.load(file)
   print(f"[load Success] success rate is: {loaded_datas["success_rate"]}")
   print(f"exicution time is :{loaded_datas["execution_time"]}")
         
        
#  Task 3: User Profile & Dynamic Welcome Message

dict_datas = {
    "user_id":101,
    "username":"HafeedaDev",
    "theme":"Dark",
    "role":"AI System Design"
 }

user_profile = "user_profile.json"

with open(user_profile, "w")as file:
    json.dump(dict_datas,file, indent=4)
print("[Success Write and json Dump]")    
  
with open(user_profile, "r")as file:
    loaded_data = json.load(file)
print(f"[Load Success] Welcome back HafeedaDev")
print(f"Role: {loaded_data["role"]} \n Active Theme {loaded_data["theme"]}")      
    







