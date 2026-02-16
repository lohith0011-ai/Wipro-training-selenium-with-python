import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.request("GET", url)

for user in response.json():
    print(user["name"], "-", user["email"])


import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}

response = requests.request("GET", url, params=params)

print("Number of posts:", len(response.json()))


import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload = json.dumps({
    "title": "Test",
    "body": "Demo",
    "userId": 1
})

headers = {
    "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)

print("Status Code:", response.status_code)

if response.status_code == 201:
    print("Created successfully")




requests.post(url, data={"name":"John"})


requests.post(url, json={"name":"John"})




import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.request("GET", url)

if response.status_code != 200:
    raise Exception("API Error!")

print("Request Successful")


import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.request("GET", url)

for user in response.json():
    print(user["username"].upper())






import requests
from requests.exceptions import Timeout

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.request("GET", url, timeout=2)
    print(response.json())
except Timeout:
    print("Request timed out")




import requests

session = requests.Session()

response1 = session.get("https://jsonplaceholder.typicode.com/users")
print(response1.status_code)

response2 = session.get("https://jsonplaceholder.typicode.com/posts")
print(response2.status_code)

print("Cookies:", session.cookies.get_dict())






import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.request("GET", url)

with open("posts.json", "w") as file:
    json.dump(response.json(), file, indent=4)

print("Saved into posts.json")



