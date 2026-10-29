

import requests


def fetch_posts(user_id):
    try:
        url ="https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url, params={"userId": user_id}, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout as e:
        print(f"Not respond server {e}")    
        return []
    except requests.exceptions.HTTPError as e:
        print(f"Http Error: {e}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Exception Error: as {e}")
        return []
    else:
        return response.json()
    finally:
        print("Request completed")

posts = fetch_posts(1)
print("user 1 posts:", len(posts))