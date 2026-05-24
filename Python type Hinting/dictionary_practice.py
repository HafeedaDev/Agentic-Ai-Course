#   task 1
#  a create function with type hint
def build_agent_profile(name: str, role: str) -> dict:
    # items assign a variable
    profile = {"name": name, "role": role}
    return profile
#  value Store to variable 
agent_profile = build_agent_profile("HafiAhamed","Ai Engineer" )
# final result
print(agent_profile)


# task2


def verify_agent_password(password: str,correct_password: str) -> bool:
 if password == correct_password:
     print("your password is correct")
     return True
     
 else:
    print("your password is not correct")
    return False
    

is_correct = verify_agent_password("hafi@kt","Hafi@kt")
print(is_correct)


# task 3

def update_agent_role(agent_data: dict,new_role: str) -> dict:
 
 agent_data["role"] = new_role
 return agent_data
my_data = {"name" : "Hafeeda", "role" : "Ai Engineer", "Company" : "Google"}


update_value = update_agent_role(my_data, "Lead Ai Specialist")
print(update_value)


# task 4

def check_system_status(memory_usage: int) ->str:
   
   if  memory_usage > 80:
      return "Critical:High memory Usage"

   elif memory_usage >= 50:
      return "Warning: Modarate memory Usage"

   else:
     return "Normal: System Healthy"

system_status = check_system_status(78)
print(system_status)


           
# task 5
def add_agent_tool(agent_profile: dict, new_tool: str)-> dict:
 agent_profile["tool"] = new_tool
 return agent_profile 
current_agent = {"name":"Ramu", "status":"Active"}

agent_data = add_agent_tool(current_agent, "web search")

print(agent_data)

# task 6

def remove_secret_key(agent_info: dict)->dict:
   agent_info.pop("secret_key")
   return agent_info

my_bot = {"bot_name": "CryptoBot", "secret_key": "XYZ123",  "version": 2.0}

update_data = remove_secret_key(my_bot)
print(update_data)


# task 7



def get_agent_location(data: dict)-> str:
   get_data = data.get("location","Unknown Location")
   return get_data

get_a = {"name":"alpha","location":"us-server"}
get_b = {"name":"Beta"}
print(get_agent_location(get_a))
print(get_agent_location(get_b))




# task 8

def get_all_Keys(data: dict) ->list:
  
  key_values = data.keys()
  return list(key_values)
 
my_agent = {"id" : 101, "name":"Jarvis", "role" :"AI"}

agent_value = get_all_Keys(my_agent)
print(agent_value)


# task 8

# a create function with typehinting
def get_all_values(data:dict) -> list:
   # store values to a variable
   item_values = data.values()
   #  reyurn the value and items convert list 
   return list(item_values)
my_agent = {"id" : 101, "name":"Jarvis", "role" :"AI"}
get_items = get_all_values(my_agent)

# final result
print(get_items)

# a create function with typehinting
def get_all_values(data:dict) -> list:
   # store items to a variable
   item_values = data.items()
   #  reyurn the items and items convert list 
   return list(item_values)
my_agent = {"id" : 101, "name":"Jarvis", "role" :"AI"}
get_items = get_all_values(my_agent)

# final result
print(get_items)



