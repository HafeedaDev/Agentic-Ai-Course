# create Custom Exception

class InvalidConfigError(Exception):
    pass

config: dict = {
    "agent_name":"Agent01",
    "max_iterations":25,
    "temperature":0.7
}

def validate_agent_config(config:dict)-> bool:

    try:
        if not config.get("agent_name"):
            raise InvalidConfigError("Agent name cannot be empty!")
        if config.get("max_iterations") <1 or config.get("max_iterations") >20:
            raise InvalidConfigError("max_iterations must be between 1 and 20!")
        if config.get( "temperature")<0 or  config.get( "temperature")>1.0:
            raise InvalidConfigError("temperature must be between 0.0 and 1.0!")
    except InvalidConfigError as e:
        print(f"ERROR: {e}")
        return False
    else:
        print("SUCCESS: Config Validated") 
        return True 
is_valid = validate_agent_config(config)
print("Is config valid?", is_valid)


