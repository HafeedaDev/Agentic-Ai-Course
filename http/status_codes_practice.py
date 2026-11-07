import  requests

codes = [200, 201, 404, 500, 401, 429, 503]

for code in codes:
    response = requests.get (f"https://httpbin.org/status/{code}", timeout=10)
    print(code, "->", response.status_code, "| ok:",response.ok)