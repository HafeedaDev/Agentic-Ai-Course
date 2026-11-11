import os
import requests
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("GITHUB_TOKEN")

if token is None:
    print("GITHUB_TOKEN not found in .env")
else:
    headers={"Authorization": f"Bearer {token}" }
    response =  requests.get("https://api.github.com/rate_limit", headers=headers)
    print( response.status_code)
    if response.ok:  
        print(response.json()["rate"]["limit"])