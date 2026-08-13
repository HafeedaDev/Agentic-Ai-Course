# create Custom Exception

class InvalidConfigError(Exception):
    pass

# Create empty list for errors

activity_log = []

config = {
    "agent_name":"AgentLogger",
    "max_iterations":25,
    "temperature":1.2
}

def validate_agent_config(config):
    try:
        if not config.get("agent_name"):
            raise InvalidConfigError("Agent name cannot be empty!")
        if config.get("max_iterations") <1 or config.get("max_iterations") >20:
            raise InvalidConfigError("max_iterations must be between 1 and 20!")
        if config.get( "temperature")<0 or  config.get( "temperature")>1.0:
            raise InvalidConfigError("temperature must be between 0.0 and 1.0!")
    except InvalidConfigError as e:
        activity_log.append(f"ERROR: {e}") 
    else:
        activity_log.append("SUCCESS: Config Validated")  
        
validate_agent_config(config)
print("Activity Log :",activity_log)    