import  requests

url = "http://127.0.0.1:8000/webhook"

data = {"action": "created", "repository": "Agentic-Ai-Course", "sender": "Hafi"}

response = requests.post(url, json=data)
print(response.status_code)