import requests

def get_todos(user_id,completed):

    try:
        url = "https://jsonplaceholder.typicode.com/todos"
        my_params = {
            "userId": user_id,
            "completed": completed
        }
        my_headers = {"User-Agent": "Learning App"}

        response = requests.get(url, params=my_params, headers=my_headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("Final URL:", response.url) 
    except requests.exceptions.Timeout as e:
        print(f"Not respond server {e}")
        return[]
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Exception Error: {e}")    
        return []
    else:
        return data
    finally:
        print("Request completed")
todos = get_todos(3, "false")  
print("Count:", len(todos))
for todo in todos:
    print("❌", todo["title"])    