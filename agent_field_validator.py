from pydantic import BaseModel, field_validator, ValidationError

class AgentConfig(BaseModel):
    agent_name: str
    api_key: str 
    temperature: float

# clean agent name  space  
    @field_validator('agent_name', mode='before')
    @classmethod

    def cleaned_agent_name(cls, value: str)-> str:
        if isinstance(value, str):
            value = value.strip().upper()
        if len(value) < 3:
           raise ValueError("It should be atleast 3 letters ")
        return value 
# clean  api_key space
 
    @field_validator('api_key', mode='before')
    @classmethod

    def cleaned_api_key(cls, value: str) -> str:
        if isinstance(value,str):
           value = value.strip()
        if not value.startswith("SK"):
            raise ValueError("API Key must start with 'SK-'")
        return value     
#  check temperature

    @field_validator('temperature', mode="after")
    @classmethod 

    def check_temperature(cls, value:float) -> float:
        if not (0.0 <= value <= 1.0):
          raise ValueError("Temperature must be between 0.0 and 1.0")
        return value

try:
    config = AgentConfig(
        agent_name="   researcher_agent   ",
        api_key="  SK-123456789abc   ",
        temperature=0.7
    )
    print("-"*50)
    print("Agent Config Success!")
    print(f"Agent Name: {config.agent_name}")
    print(f"API Key: {config.api_key}")
    print(f"Temperature: {config.temperature}")
    print("-"*50)
except ValidationError as e:
    print(f"Validation Error:\n{e}")     
    

    
