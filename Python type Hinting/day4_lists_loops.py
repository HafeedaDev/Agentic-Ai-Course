#  task 1.
def create_agent_list(agent1: str, agent2: str, agent3: str) -> list:
    return [agent1, agent2, agent3]


list_items = create_agent_list("Alpha", "Beta", "Gamma")
print(list_items)


# task 2


# create a function with typehinting
def add_new_agent(current_agent: list, new_agent: str) -> list:
    #   appent a new agent
    current_agent.append(new_agent)
    return current_agent


agent_list = ["Hari", "Raju", "Jose"]
update_list = add_new_agent(agent_list, "Gopal")
print(update_list)


# task 3
def convert_to_uppercase(agent_name: str) -> str:
    return agent_name.upper()


print(convert_to_uppercase("i am a ai engineer"))


# task 4


def get_agent_count(all_agents: list) -> int:
    return len(all_agents)


my_team = ["Alpha", "Beta", "gamma"]
print(get_agent_count(my_team))


# Task 5


# create a function with typehinting
def broadcast_agent(agent_list: list) -> None:
    # loop the items
    for agent in agent_list:

        print(f"{agent} is ready")


my_team = ["Ajay", "Hari", "Raju"]
# final result
broadcast_agent(my_team)


# task 6


# create a function with typehinting
def get_agent_role(agent_dict: dict, key_name: str) -> str:
    return agent_dict.get(key_name)


current_status = {"name": "Alpha", "role": "coder"}

agent_role = get_agent_role(current_status, "role")
print(agent_role)


# task 7
def find_agent_power(agent_data: dict, search_key: str) -> int:
    return agent_data.get(search_key)


test_agent = {"name": "Jarvis", "power": 98}
test_value = find_agent_power(test_agent, "power")
print(test_value)


# task 8


def get_secure_role(profile: dict, key: str) -> str:
    return profile.get(key, "Access Denied")


spy_profile = {"name": "Athan", "role": "Spy"}
get_value = get_secure_role(spy_profile, "secret_code")
print(get_value)


# task 9
# create a function with typehinting
def clean_agent_list(raw_list: list) -> tuple:
    #    clean data from dirty_list using set()
    new_set = set(raw_list)
    print(type(new_set))
    tuple_value = tuple(new_set)
    print(type(tuple_value))
    return tuple_value


dirty_list = ["Hari", "Raju", "Hari", "Gopal"]
clean_value = clean_agent_list(dirty_list)
print(clean_value)


   
