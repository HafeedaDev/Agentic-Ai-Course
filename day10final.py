from pydantic import BaseModel
from typing import List
# Day 10: Advanced Practice Task

# Task7: LLM Output Parser(Nested Model)

class TokenUsage(BaseModel):
    prompt_token: int
    completion_tokens:int

class AIResponse(BaseModel):
    response_id:str
    content:str
    usage:TokenUsage


llm_output = {
    "response_id": "res_9921",
    "content": "The weather is sunny today",
    "usage": {
        "prompt_token": 15,
        "completion_tokens": 20
    }
}
    
ai_response_data = AIResponse(**llm_output)

print("AI response data",ai_response_data)


# Task 8:Multiple  Agents Validator (List of Models)

class AgentProfile(BaseModel):
    agent_id: int
    role:str
    is_active:bool

class SystemConfig(BaseModel):
    agents:list[AgentProfile]

network_data = {
    "agents": [
        {"agent_id": 1, "role": "Manager", "is_active": True},
        {"agent_id": 2, "role": "Tester", "is_active": "yes"},
        {"agent_id": 3, "role": "Writer", "is_active": False}
    ]
}  

system_config_data = SystemConfig(**network_data)

print("System_config_data: ", system_config_data)
