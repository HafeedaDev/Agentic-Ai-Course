
import requests

def get_comments(postId):

    try:
        url = "https://jsonplaceholder.typicode.com/commentsvvvv"
        my_params = {
            "postId": postId
        }
        response = requests.get(url, params=my_params, timeout=10)
        response.raise_for_status()
    
    except requests.exceptions.Timeout as e:
        print(f"Not respond server {e}")
        return []
    except requests.exceptions.HTTPError as e:
        print(f" HTTP Error {e}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Exception error {e}")
        return []
    else:
        data = response.json() 
        return data   
    finally:
        print("Request completed")

      

comments = get_comments(2)
print("Count:", len(comments))
for comment in comments:
    print(comment["email"]) 