


from pydantic import BaseModel

# 1. Inner Model
class TaskConfig(BaseModel):
    max_cost_usd: float
    requires_gpu: bool

# 2. Outer Model
class TaskRequest(BaseModel):
    task_id: str
    category: str      # "code", "search", "database"
    priority: int      # 1 to 5 (5 is highest)
    config: TaskConfig # Nested Model

# 3. Incoming Raw API Stream Data
raw_incoming_tasks = [
    {
        "task_id": "TSK-101",
        "category": "code",
        "priority": 5,
        "config": {"max_cost_usd": 0.05, "requires_gpu": False}
    },
    {
        "task_id": "TSK-102",
        "category": "search",
        "priority": 2,
        "config": {"max_cost_usd": 0.01, "requires_gpu": False}
    },
    {
        "task_id": "TSK-103",
        "category": "code",
        "priority": 4,
        "config": {"max_cost_usd": 0.50, "requires_gpu": True}
    },
    {
        "task_id": "TSK-104",
        "category": "database",
        "priority": 1,
        "config": {"max_cost_usd": 0.02, "requires_gpu": False}
    },
    {
        "task_id": "TSK-105",
        "category": "code",
        "priority": 3,
        "config": {"max_cost_usd": 0.08, "requires_gpu": False}
    }
]

high_priority_code_tasks = {
    item["task_id"]:TaskRequest(**item)
    for item in raw_incoming_tasks
    if item["category"] == "code" and item["priority"] >= 4
}
print("="*50)
for task_id, task_obj in high_priority_code_tasks.items():
    print(f"Task Id: {task_id} | Priority: {task_obj.priority} | MaxCost(USD): {task_obj.config.max_cost_usd} | Requires GPU Status :{task_obj.config.requires_gpu}")
print("="*50)



