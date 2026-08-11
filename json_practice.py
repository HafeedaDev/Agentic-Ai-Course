
import json

# 1. Original Python Dictionary
agent_data = {
    "agent_name": "SearchAgent",
    "status": "active",
    "tools": ["google_search", "python_interpreter"],
    "max_iterations": 5,
    "is_certified": True
}

print("=== 1. json.dumps() : Python Dict to JSON String ===")
json_string = json.dumps(agent_data, indent=4)
print(json_string)
print("Type:", type(json_string))


print("\n=== 2. json.loads() : JSON String to Python Dict ===")
parsed_dict = json.loads(json_string)
print("Agent Name:", parsed_dict["agent_name"])
print("Type:", type(parsed_dict))


print("\n=== 3. json.dump() : Writing Python Dict to .json File ===")
file_name = "agent_config.json"
with open(file_name, "w") as file:
    json.dump(agent_data, file, indent=4)
print(f"Data saved successfully to '{file_name}'")


print("\n=== 4. json.load() : Reading from .json File ===")
with open(file_name, "r") as file:
    loaded_data = json.load(file)

print("Loaded Tools:", loaded_data["tools"])
print("Is Certified?", loaded_data["is_certified"])