import requests

url = "https://dogs.ie/"

response = requests.get(url)
data = response.json()

print(data)