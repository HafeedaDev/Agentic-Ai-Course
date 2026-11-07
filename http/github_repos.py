
import requests


def get_all_repos(username):

    try:
        url = f"https://api.github.com/users/{username}/repos"
        page= 1
        all_repos =[]
        my_header = {"User-Agent":"Learning_App", "Accept": "application/vnd.github+json"}
        while True:
            my_params = {"page":page,"per_page":30, "sort": "updated"}
            response = requests.get(url, params=my_params, headers= my_header, timeout=10)
            response.raise_for_status()
            repos = response.json()
            if not repos:
                break
            print(f"--- Page {page} ---") 
            for repo in repos:
                print(f"repo name: {repo['name']}")
            all_repos.extend(repos)    
            print(f"Total repos: {len(all_repos)}")
            print("New URL:",response.url)
            page +=1
    except requests.exceptions.Timeout as e:
        print(f"Time Error {e}")
        return []

    except requests.exceptions.HTTPError as e:
        if e.response is not None:
         print("Status Code:", e.response.status_code)   
        print(f"HTTP Error: {e}")
        return []

    except requests.exceptions.RequestException as e:
        print(f"Request failed:{e} ")    
        return []
    
    else:
        return all_repos

    finally:
        print("Requests Finished")


for username in ["HafeedaDev", "this-user-does-not-exist-xyz-12345"]:
    repo_datas = get_all_repos(username)
    print(f"{username}: {len(repo_datas)} repos")
    print("-" * 30)
  

        



























