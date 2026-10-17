import requests

def fetch_user_posts(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    query_params = {"userId":user_id}
    try:
        response = requests.get(url, params=query_params,timeout=5)
        response.raise_for_status()
        post = response.json()
        return post
    except requests.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.ConnectionError:
        print("Connection Error: Internet not available")
    except requests.Timeout:
        print("Timeout Error:Late server response ")
    except Exception as err:
        print(f"An error occurred: {err}")    

    return None

# Call function


user_id = input("Enter your Id: ")
posts_data = fetch_user_posts(user_id)

if posts_data:
    print(f"Total Posts: {len(posts_data)}")
    print(f"Second Post Title: {posts_data[1]['title']}")





































