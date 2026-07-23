
# filter data using filter and lambda

# Raw data
agent_logs = [
    {"agent_name": "Alpha-Agent", "uptime_hours": 120, "status": "active"},
    {"agent_name": "Beta-Agent", "uptime_hours": 5, "status": "idle"},
    {"agent_name": "Gamma-Agent", "uptime_hours": 340, "status": "active"},
    {"agent_name": "Delta-Agent", "uptime_hours": 0, "status": "offline"},
    {"agent_name": "Epsilon-Agent", "uptime_hours": 72, "status": "active"}
]

filtered_data = filter(lambda emp: emp["status"]=="active" and emp["uptime_hours"] >50, agent_logs )

final_list = list(filtered_data)

print(final_list)