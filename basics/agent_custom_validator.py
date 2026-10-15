config ={
    "agent_name":"ReasearcherAgent",
    "max_iterations":5,
    "temperature":-5
}
def validate_agent_config(config):
    try:
        if not config.get("agent_name"):
            raise ValueError("Agent name  cannot be  empty!")
        if config.get("max_iterations")<1 or  config.get("max_iterations")>20:
            raise ValueError("max_iterations must be between 1 and 20!")  
        if config.get("temperature")<0.0 or  config.get("temperature")>1.0:
            raise ValueError("temperature must be between 0.0 and 1.0!")   
    except ValueError as e:
         print(f"Validation Error: {e}")
    else:
        print("Config validated Successfully!")
    finally:
        print("Validation process finished")    
validate_agent_config(config)
                 

