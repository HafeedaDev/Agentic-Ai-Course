
import json

# 1 Dictionary Basics
# 
ai_agent = {
    "name": "Tirur_agent",
    "role": "AI Engneer",
    "status":"Active"
} 

print("Feature 1: Dict Basics")
print("Agent Name:", ai_agent["name"])

# 2.JSON parsing
llm_response = '{"model": "GPT-4", "tokens": 150}'

parsed_data = json.loads(llm_response)

print("\n --- Feature 2: JSON Parsing----")

print("Model Used:", parsed_data["model"])

# 3.Modify & Add

ai_agent = {
    "name": "Tirur_Agent",
    "role": "AI Engineer"
}

# add new value

ai_agent["status"] = "Active"

# value change remaining value

ai_agent["role"] = "Lead AI Engineer"

print("---Feature 3: Add & Modify")

print(ai_agent)

# 4.dont get error to take data .get()

print("/n ----Feature 4: Safe Get---")
print("model:", ai_agent.get("model"))

# 5. Dictionary convert to JSON 

agent_json = json.dumps(ai_agent)

print("/n---Feature 5: Dictionary to JSON-----")
print(agent_json)

# Task1: API Response Parsing

json_data = '{"status": "success", "response": "Hello from Gem"}'

print(json_data)


# Task 1:

json_data = '{"status": "success", "response": "Hello from Gem"}'

parsed_dict = json.loads(json_data)

print(parsed_dict["response"])



# Task 2: Update Agent Status 
agent_profile = {
    "agent_name": "Search_Bot",
    "status": "Offline"
}
agent_profile["status"] = "Active"
agent_profile["version"] = 1.0

print(agent_profile)

# Task 3 Safe Memory Fetch:
llm_config = {
    "model_name": "Llama-3",
    "max_tokens": 512
}
print(llm_config.get("temperature", 0.7))

# Task 4: Package payload(Dict to JSON)
payload_dict = {
    "user_id": 101,
    "command": "start_task"
} 

dict_to_json = json.dumps(payload_dict)

print(dict_to_json)


# Task 5:Advanced LLM Parser&Status Updater

raw_response = '{"agent_name": "Writer_Bot", "agent_status": "Processing", "tokens_used": 240}'

raw_response_dict = json.loads(raw_response)

print("JSON string convert to dictionary", raw_response_dict)

raw_response_dict["agent_status"] ="Completed"
print("updated value", raw_response_dict)

raw_response_dict["error_log"] = None

print(raw_response_dict)


# dictionary convert to JSON String

dict_to_json = json.dumps(raw_response_dict)

print(dict_to_json)


# Task 6: Safe Guard Config  Reader

agent_config = {
    "model": "Claude-3",
    "temperature": 0.2
}

print(agent_config .get("max_tokens",1000))
print(agent_config .get( "temperature"))

