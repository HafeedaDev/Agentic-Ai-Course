from typing  import List, Dict, Optional

# Sample Agent State Data
agent_state: Dict[str, object] = {
    "agent_name":"ReasearcherAgent",
    "completed_tasks":["Scrape Web", "Summarize Paper"],
    "current_task":"Generate Report ", #Optional
    "retry_count":0

}

# create function with Type Hinting
def get_agent_summary(state:Dict[str,object])-> str:
    name:str = state.get( "agent_name")
    tasks:List[str] = state.get("completed_tasks",[])
    task_count = len(tasks)
    return f"Agent {name} has completed {task_count} tasks"

summary = get_agent_summary(agent_state)
print(summary)
