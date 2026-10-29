import requests

def get_post(post_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout as e:
        print(f"Dont get respond {e} ")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Http Error {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error msg {e}")
        return None
    else:
        return response.json()
    finally:
        print("finished Requests")

# print(get_post(999)) 
# print(get_post(5))


post_1 = get_post(1)
print("post 1:", post_1)