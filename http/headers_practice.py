import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
# response.raise_for_status()

# print(type(response.headers))

# print(response.headers["Content-Type"])
# print(response.headers["content-type"])


my_headers = {
    "User-Agent": "hafeeda-learning-app",
    "Accept": "application/json"
}

response = requests.get("https://httpbin.org/headers", headers=my_headers, timeout=10)
response.raise_for_status()

print(response.json())
