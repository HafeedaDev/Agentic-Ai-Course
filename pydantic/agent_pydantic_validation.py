from pydantic import BaseModel, Field
from typing import List, Optional


class AgentState(BaseModel):
    agent_name: str                        # Type Hint: String
    completed_tasks: List[str] = []        # Type Hint: List of strings
    current_task: Optional[str] = None     # Type Hint: Optional string
    retry_count: int = Field(default=0, ge=0)  # Type Hint: Integer 


# 2. Correct Data :
print("--- 1. Testing Valid Data ---")
try:
    valid_agent = AgentState(
        agent_name="SearchAgent",
        completed_tasks=["Google Search", "Scrape Content"],
        current_task="Summarize Data",
        retry_count=2
    )
    print("Success! Created Agent State:")
    print(valid_agent)
except Exception as e:
    print(f"Error: {e}")


# 3. Wrong Data (Type Mismatch) :
print("\n--- 2. Testing Invalid Data (Type Validation Test) ---")
try:
    
    invalid_agent = AgentState(
        agent_name="SearchAgent",
        retry_count="Three"  
    )
except Exception as e:
    print("Pydantic Validation Error Caught Successfully:")
    print(e)