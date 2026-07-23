from pydantic import BaseModel ,RootModel, ValidationError,Field
from typing import List

# create pydentic Model
class Ticket(BaseModel):
    ticket_id: str
    user_query: str
    priority:str
    estimated_hours: float  = Field(gt=0) # must be strictly >0

class AIAgentTickets (RootModel[List[Ticket]]):
    pass

    print("="*50)
    print("Capstone Task: AI aGENT tICKET & Task Dispatcher")
    print("="*50)
# Create A function 

def aiAgent_ticket_dispatcher(ticket_data: List[Ticket]):
  
    if not ticket_data:
        print("Not found data")
    else:
        for data in ticket_data:  
            print(f"ID: {data.ticket_id:<10}|User query: {data.user_query:<20}| Priority : {data.priority:<10}| Estimate Hours:{data.estimated_hours} ")
# Raw Data
raw_tickets_data = [
    {"ticket_id": "TCK-101", "user_query": "  Fix login bug  ", "priority": "HIGH", "estimated_hours": 3},
    {"ticket_id": "TCK-102", "user_query": "Optimize database", "priority": "medium", "estimated_hours": 2}, # Invalid hours!
    {"ticket_id": "TCK-103", "user_query": "Update UI theme", "priority": "LOW", "estimated_hours": 1},
    {"ticket_id": "TCK-104", "user_query": "Deploy AI model", "priority": "CRITICAL", "estimated_hours": 8},
    {"ticket_id": "TCK-105", "user_query": "Fix API pipline", "priority": "HIGH", "estimated_hours": 4}, # Empty query!
]

# Step 3: Validation with Try - Exception

try:
    agent_ticket_data = AIAgentTickets.model_validate(raw_tickets_data)
    validated_data = agent_ticket_data.root

    data_comprehension = [
        Ticket(
            ticket_id = agent.ticket_id,
            user_query = agent.user_query.strip(),
            priority = agent.priority.upper(),
             estimated_hours = agent.estimated_hours/2


        )
        for agent in validated_data
    ]

    filtered_data = filter( lambda emp : emp.priority in ["HIGH", "CRITICAL"] and emp.estimated_hours<=3,data_comprehension)

    filtered_list_data = list(filtered_data)

    aiAgent_ticket_dispatcher(filtered_list_data)
    print("="*50)
except ValidationError as e:
    print(f"Got validation error {e}")  
except Exception as e :
    print(f"Got Error {e}")
