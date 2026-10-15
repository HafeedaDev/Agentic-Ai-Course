
from pydantic import BaseModel

# 1. Inner Model (Metrics)
class AgentMetrics(BaseModel):
    latency_ms: int
    memory_mb: float

# 2. Outer Model (Agent Node)
class AgentNode(BaseModel):
    node_id: str
    status: str       # "online", "offline", "degraded"
    metrics: AgentMetrics # Nested Model

# 3. Incoming Stream Data
raw_cluster_data = [
    {
        "node_id": "NODE-01",
        "status": "online",
        "metrics": {"latency_ms": 120, "memory_mb": 512.5}
    },
    {
        "node_id": "NODE-02",
        "status": "offline",
        "metrics": {"latency_ms": 0, "memory_mb": 0.0}
    },
    {
        "node_id": "NODE-03",
        "status": "online",
        "metrics": {"latency_ms": 450, "memory_mb": 1024.0}
    },
    {
        "node_id": "NODE-04",
        "status": "online",
        "metrics": {"latency_ms": 85, "memory_mb": 256.0}
    }
]
healthy_agents_map = {
    item["node_id"]:AgentNode(**item)
    for item in raw_cluster_data
    if item["status"] == 'online' and item["metrics"]["latency_ms"]<200
    
}
print("="*50)
for node_id, node_obj in healthy_agents_map.items():
    print(f"Node Id : {node_id}| Latency :{node_obj.metrics.latency_ms}| Memory (MB) :{node_obj.metrics.memory_mb}")

print("="*50)
