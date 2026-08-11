import json

feedback_data = {
    "feedback_id":101,
   "user_id":"USR_892",
   "rating":4.8,
   "comments":["Greatresponse","Fast exicution"],
   "is_resolved":False
}

print("step 1: Serialize python dictionary to Json string")
feedback_data_string = json.dumps(feedback_data)
print(f"Json string:",feedback_data_string)


print("step 2: Deserialize Json string to python dictionary")
load_dict = json.loads(feedback_data_string)
print(f"Converted Python Dictionary,Comments:,{load_dict["comments"]}")
print(f"Rating:{load_dict["rating"]}")

print("Step 3: Sve python dictionary to JSON file")
filename = "user_feedback.json"
with open(filename, "w")as file:
    json.dump(feedback_data,file, indent=4)

print(" step 4:Read JSON file into Python dictionary")
with open(filename, "r")as file:
    loaded_data = json.load(file)
print(f"User Id:{loaded_data["user_id"]}")
print(f"Is resolved:{loaded_data["is_resolved"]}")    

