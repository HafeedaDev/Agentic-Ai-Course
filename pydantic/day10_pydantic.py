from pydantic import BaseModel

class AgentConfig(BaseModel):
    agent_name: str
    max_tokens:int
    temperature: float = 0.7

print("----Feature 1:-----")
good_data = {
    "agent_name":"Writer Bot",
    "max_tokens":1500
}
# dictionary convert to model 

config = AgentConfig(**good_data)
print(config)
print("Agent Name:", config.agent_name)
print("Defaul Temperature:", config.temperature)

print("\n Feature 2: (Try-Except)----")
try:
    bad_data = {
        "agent_name": "Error_Bot",
        "max_tokens":"More"
    }
    wrong_config = AgentConfig(**bad_data)
except Exception as e:
    print("pedentic got error")    
    print(e)


# Task 1:PromptSchema

class PromptSchema(BaseModel):
    template_name: str
    max_input_chars: int

good_prompt = { 
    "template_name": "Schema_writer",
    "max_input_chars":2000

}
prompt = PromptSchema(**good_prompt)
print(prompt)
print("Template Name:", prompt.template_name)


# Task 2: Default System Instruction

class AgentInstruction(BaseModel):
    role: str
    instruction: str = "You are a helpful AI Assistent"

custom_agent = {
    "role": "Code_Reviewer"
}

agent = AgentInstruction(**custom_agent)

print(agent)

# Task 3: The AI Safe Guard (Try-Exept Challenge)

print("------Try Except-----")

try:
    bad_agent_data = {
        "template_name": "Ghost_Agent",
        "max_input_chars": "long data"
    } 

    wrong_agent_data = PromptSchema(**bad_agent_data)
except Exception as e:
    print("pedentic got error")    
    print(e)



# Task 4:AI Agent Profile Schema

class AgentProfile(BaseModel):
    agent_id: int
    role: str
    is_active:bool

good_agent = {
    "agent_id": 101,
    "role": "Data_Analyst",
    "is_active": True
}

agent_profile = AgentProfile(**good_agent)
print(agent_profile)

# Task 5: The Smart Converter Challenge

mixed_data = {
    "agent_id": "550",    
    "role": "Researcher",
    "is_active": "True"   
}

converted_profile = AgentProfile(**mixed_data)
print(converted_profile)

# Task 6: Secure the LLM Response (Try-Except)
print("------Try Except task6-----")

try:
    corrupted_llm_data = {
    "agent_id": 999,
    "role": "Creative_Writer",
    "is_active": "Hello" 
    }
    bad_data = AgentProfile(**corrupted_llm_data)
    print(bad_data)

except Exception as e:
    print("Got error")
    print(e)    