import requests

# def fetch_sample_data():

# #    free testing Api endpoint
#     url = "https://jsonplaceholder.typicode.com/posts/1"

#     print("Sending GET request to external API..")
#     response = requests.get(url)

#     # check the status code
#     print(f"Status code: {response.status_code}")
#     if response.status_code == 200:

#         data = response.json() # json data convert to dictionary
#         print("--- Data Received ---")
#         print(f"Title: {data['title']}")
#         print(f"Body: {data['body']}")
#     else:
#         print(f"Failed to fetch data. Error code: {response.status_code}")
# if __name__=="__main__":
#     fetch_sample_data()



# def send_sample_data():
#     url = "https://jsonplaceholder.typicode.com/posts"

#     my_data = {
#         "userId":1,
#         "title":"My Data",
#         "body":"Learning HTTP POST request in Python"
#     }

#     response = requests.post(url, json=my_data)

#     if response.status_code == 201:
#         datas = response.json()
#         print("--Data Posted--")

#         print(f"Title: {datas['title']}")
#         print(f"Body: {datas['body']}")
#     else:
#         print(f"Failed Post data: {response.status_code}")


# if __name__ == "__main__":
#     send_sample_data()            

# def update_sample_data():
#     url = "https://jsonplaceholder.typicode.com/posts/2"
    
#     updated_data = {
#         "id": 1,
#         "title": "Updated Title",
#         "body": "Updated body text",
#         "userId": 1
#     }
    
#     response = requests.put(url, json=updated_data)
    
#     if response.status_code == 200:
#         datas = response.json()
#         print("--Data Updated--")
#         print(f"Title: {datas['title']}")
#     else:
#         print(f"Failed: {response.status_code}")

# if __name__ == "__main__":
#     update_sample_data()

def delete_sample_data():
    url = "https://jsonplaceholder.typicode.com/posts/3"
    response = requests.delete(url)

    if response.status_code == 200:
        print("Sucessfully Deleted")
    else:
        print(f"Failed to delete :{response.status_code}")   

if __name__ == "__main__":
    delete_sample_data()
















