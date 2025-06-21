
#?  🎯 Challenge
#? Fetch and display a webpage’s content 

import requests

URL =  "https://api.adviceslip.com/advice"
response = requests.get(URL)
print(response.content)
data = response.json()

print("\n💬", data["slip"]["advice"])
