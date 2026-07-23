
task_queue = [
    {"task_id": "TASK_101", "priority": "high", "estimated_minutes": 45},
    {"task_id": "TASK_102", "priority": "low", "estimated_minutes": 15},
    {"task_id": "TASK_103", "priority": "high", "estimated_minutes": 10},
    {"task_id": "TASK_104", "priority": "medium", "estimated_minutes": 60},
    {"task_id": "TASK_105", "priority": "high", "estimated_minutes": 90}
]

filtered_data = filter( lambda emp: emp['priority'] == 'high' and emp['estimated_minutes'] >= 45, task_queue)

filtered_data_list = list(filtered_data)
print(filtered_data_list)