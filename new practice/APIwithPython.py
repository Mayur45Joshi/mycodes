import requests
import json

url="https://jsonplaceholder.typicode.com/users"

#>>>>>>>>>> GET Request>>>>>>>>>>>>>>>>>>
response=requests.get(url)
print(response)
print(response.status_code)
print(response.json())

assert response.status_code==200, "status code is not 200"
data=response.json()
assert len(data)>0, "response not empty"
assert "name" in data[0], "name field id required"

#>>>>>>>>> POST Request >>>>>>>>>

payload={
    "title": "Test Post",
    "body": "This is a sample API test",
    "userId": 1
}

headers={"Content-Type" : "application/json"}
response=requests.post(url,data=json.dumps(payload),headers=headers)
print(response.status_code)
print(response.json())

#>>>>>>>>> PUT Request >>>>>>>>

url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"title": "Updated Title"}

response=requests.put(url,json=payload)
print(response.status_code)
print(response.json())

#>>>>>>>>Patch Reauest>>>>>>>>

url = "https://jsonplaceholder.typicode.com/posts/1"

# Partial update (only update title)
payload = {
    "title": "Updated title using PATCH"
}
# You can pass data as json directly
response = requests.patch(url, json=payload)
print("Status Code:", response.status_code)
print("Response Body:", response.json())


#>>>>>>>>>>>> DElete Request >>>>>>>>>>>>>>.

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print(response.status_code)

#>>>>>>>. Headers Auths >>>>>>>

url = "https://api.github.com/user"
headers = {"Authorization": "Bearer <your_token>"}
response = requests.get(url, headers=headers)
print(response.json())

#Query parameters
response = requests.get("https://api.agify.io", params={"name": "mayur"})
print(response.json())

#>>>>>>Handle Response Time & Headers>>>>>>>>>>>..

response = requests.get("https://jsonplaceholder.typicode.com/posts")

assert response.elapsed.total_seconds() < 2, "Response took too long"
assert response.headers["Content-Type"] == "application/json; charset=utf-8"

