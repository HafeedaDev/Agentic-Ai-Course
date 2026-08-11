import json
order_data = {
    "order_id": 501,
    "customer_name": "Faris",
    "items": ["Laptop", "Mouse", "Keyboard"],
    "total_amount": 65000.50,
    "is_paid": True
}
print("=== 1. json.dumps() : Python Dict to JSON String ===")
data_string = json.dumps(order_data, indent=4)
print(data_string)

print("\n=== 2. json.loads() : JSON String to Python Dict ===")
load_dict = json.loads(data_string)
print("Customer Name:",load_dict["customer_name"])
print("Type:2", type(load_dict["customer_name"]))
print("Items:",load_dict["items"])
print("Type:2", type(load_dict))


print("\n=== 3. json.dump() : Writing Python Dict to .json File ===")
file_name = "agent_order_data.json"
with open(file_name,"w")as file:
    json.dump(order_data,file, indent=4)
    print(f"Data saved successfully,{file_name}")

print("\n=== 4. json.load() : Reading from .json File ===")
with open(file_name, "r")as file:
    loaded_data = json.load(file) 
    print(f"Items: {loaded_data["items"]}")   
    print(f"Toatal Amount: {loaded_data["total_amount"]}")