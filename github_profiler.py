import requests

# print("Project Title: Github User & Repository Profiler")

# def user_fetching(username):
   

#     url_profile = f"https://api.github.com/users/{username}"
#     url_repos = f"https://api.github.com/users/{username}/repos"

#     query_params={
#     'sort':'updated',
#     'direction':'desc',
#     'per_page':5
#     }
#     try:
#         response = requests.get(url_repos, params=query_params)
#         response.raise_for_status()
#         repo_data = response.json()
#         response = requests.get(url_profile)
#         response.raise_for_status()
#         profile_data = response.json()
#         return profile_data,repo_data
    
#     except requests.HTTPError as http_err:
#         print(f"HTTP Error:can't found username {http_err}")
#     except requests.ConnectionError:
#         print("Connection Error: Internet not available")
#     except Exception as err:
#             print(f"An error occurred: {err}") 
#     return None              

# username = input("Enter GitHub Username: ")
# profile_data, repo_data = user_fetching(username)

# print("----User Profile----")

# if profile_data:
#      print(f"Name :{profile_data['name']}")
#      print(f"Public Repos Count: {profile_data['public_repos']}")
#      print(f"Followers Count:  {profile_data['followers']}")

# print("----Recent Repos----")
# for repo in  repo_data:
#      print(f"Repo: {repo['name']}| Stars: {repo.max['stargazers_count']}")


     
print("Topic- API Data Filtering & Max Star Analysis")

def find_max_stargazers_count(username):
    repo_url = f"https://api.github.com/users/{username}/repos"

    repo_list = []

    try:
        response = requests.get(repo_url)
        response.raise_for_status()
        val_data = response.json()
        max_value = max(val_data, key=lambda repo:repo['stargazers_count']) 
        return max_value
        
    except Exception as e:
        if repo_list == None: 
            print(f"No public repositories found! {e}")

final_data = find_max_stargazers_count(name)

if final_data:
    print(f"Repo Name: {final_data['name']} | Max-stargazers: {final_data['stargazers_count']}")



