import requests

#url = 'https://www.gmit.ie'

#response = requests.get(url)

#print(response.status_code)
#print (response.headers)

url = 'http://127.0.0.1:5000/cars'
data = {'reg':'123','make':'Vw','model':'t5','price':21000}

response = requests.post(url, json = data)

print(response.status_code)
print(response.json)