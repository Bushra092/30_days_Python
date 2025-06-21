import requests

URL = "https://catfact.ninja/fact"
response = requests.get(URL) 
res_data = response.json()
print(res_data)