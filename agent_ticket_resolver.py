from pydantic import BaseModel, RootModel, ValidationError
from typing import List

# Pydantic Model Definition
class AgentTicketModel(BaseModel):
    agent_id:int
    agent_name: str
    team: str
    solved_tickets: int

# All list validate using RootModel    
class AgentTicketList(RootModel[List[AgentTicketModel]]):
    pass

def print_star_agents(star_list: List):
    print("="*50)
    print("STAR PERFORMERS ALERT (>= 15 TICKETS SOLVED)")
    print("="*50)
    if not star_list:
        print("Not found data")
    else:
        for agent in star_list:
            print(f"ID: {agent.agent_id} | Name: {agent.agent_name:<10} | Team: {agent.team:<10} | Ticket: {agent.solved_tickets}")    

ticket_data_raw = [
    {"agent_id": 301, "agent_name": "Sam", "team": "Billing", "solved_tickets": 12},
    {"agent_id": 302, "agent_name": "Kim", "team": "Technical", "solved_tickets": 22},
    {"agent_id": 303, "agent_name": "Robin", "team": "Security", "solved_tickets": 18},
    {"agent_id": 304, "agent_name": "Sana", "team": "Billing", "solved_tickets": 9},
    {"agent_id": 305, "agent_name": "Tara", "team": "Technical", "solved_tickets": 15}
]

try:
     validated_ticket_data = AgentTicketList.model_validate(ticket_data_raw)

     actual_ticket_data =   validated_ticket_data.root
     
     solved_ticket_data = [agent for agent in actual_ticket_data if agent.solved_tickets >=15]

     print_star_agents(solved_ticket_data)
     print("="*50)

except ValidationError as e:
    print("pydantic validation is fail")

except Exception as e:
    print("Error {e}")    