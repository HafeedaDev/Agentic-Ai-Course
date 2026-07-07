
from pydantic import BaseModel, ValidationError


# Task 1

# child pydantic Model
class AgentSystemConfig(BaseModel):
    llm_model: str
    temperature: float
    max_loops: int

# Parent pydantic Model

class AiAgentFleet(BaseModel):
    agent_id: int
    agent_name: str
    system_config: AgentSystemConfig

# Nested Raw Data
agent_raw_data = {
  "agent_id": 501,
  "agent_name": "Rakesh",
  "system_config": {
      "llm_model": "gpt-4o",
      "temperature":0.7,
      "max_loops":5
  }
}


# validation through pydantic model

try:
    ai_agent_data = AiAgentFleet(**agent_raw_data)
    agent_dict = ai_agent_data.model_dump()
    for key, value in agent_dict.items():
        if isinstance(value, dict):
              for sub_key, sub_value in value.items():
                   print(f"{sub_key.replace('_', ' ').title()}: {sub_value}")
        else:
             print(f"{key.replace('_', ' ').title()}: {value}")
                        
except ValidationError as e:
     print("pydantic validation is fail{e}")
except Exception as e:
      print("got error {e}")  



# Task 2

# Data Validation and Custom Formatting using Pydantic and Functions


agent_raw_data = {
    "agent_id": 999,
    "agent_name": "Vikram",
    "system_config": {
        "llm_model": "deepseek-r1",
        "temperature": 0.9,
        "max_loops": 7
    }
}

def print_agent_details(agent_dict: dict):
        print("="*50)
        for key, value in ai_raw_dict.items():
            if isinstance (value, dict):
                for nxt_key, nxt_value in value.items():
                    print(f"{nxt_key.replace('_',' ').title()}: {nxt_value}")
            else: 
                print(f"{key.replace('_',' ').title()}: {value}")
        print("="*50)  

try:
        ai_raw_data = AiAgentFleet(**agent_raw_data)
        ai_raw_dict = ai_raw_data.model_dump()    
        print_agent_details(ai_raw_dict)     
except ValidationError as e:
        print("pydantic validation is fail{e}")                     
except Exception as e :
        print("got error {e}")
        
                    
