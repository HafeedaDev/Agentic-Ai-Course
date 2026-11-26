import requests
URL = "http://127.0.0.1:8000/webhook/order"

orders = [
    {"order_id": "A101", "customer_email": " ANU@GMAIL.COM ", "quantity": 2, "price": 250, "total": 500},  
    {"order_id": "A102", "customer_email": "ravi@gmail.com", "quantity": 0, "price": 250, "total": 0},     
    {"order_id": "A103", "customer_email": "sara@gmail.com", "quantity": 2, "price": 250, "total": 400},
    {"order_id": "A104", "customer_email": "x@gmail.com", "quantity": 1, "price": 100},
    {"order_id": "A105", "customer_email": "ravi.gmail.com", "quantity": 1, "price": 100, "total": 100},
    {"order_id": "A106", "customer_email": "big@gmail.com", "quantity": 5, "price": 300, "total": 1500},
     
]

for order in orders:
    response = requests.post(URL, json=order, timeout=5)
    print(order["order_id"], "->", response.status_code, response.json())
    