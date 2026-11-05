import requests

# pagination

url = "https://jsonplaceholder.typicode.com/posts"
page = 1
all_posts = []


while True:
    my_params = {
        "_page" : page,
        "_limit":30

    }
    response =  requests.get(url, params=my_params,timeout=10)
    response.raise_for_status()
    posts = response.json()

    if not posts:
        break

    all_posts.extend(posts)
    print(f"page {page} {len(posts)}  posts")
    page += 1
  
print(f"Total Post: {len(all_posts)}")