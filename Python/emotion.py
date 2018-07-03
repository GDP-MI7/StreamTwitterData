import requests
import json

response = json.loads(requests.post("https://apis.paralleldots.com/v3/emotion", data={ "api_key": "h1fPGh0H5LvtHU5LhaEnlhITrHLPSYNHbZTsyusz51s", "text": "I am trying to imagine you with a personality."}).text)

print(response)