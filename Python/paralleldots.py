import requests
import json
input = open("sample.txt", "r")
for i in input.readlines():
    response = json.loads(requests.post("https://apis.paralleldots.com/v3/sentiment", data={ "api_key": "h1fPGh0H5LvtHU5LhaEnlhITrHLPSYNHbZTsyusz51s", "text": i, "lang_code": "en" }).text)
    print(response)

# response_batch = requests.post("https://apis.paralleldots.com/v3/sentiment_batch", text={ "api_key": "ABCdef123MNO456PQR789xyz", "text": json.dumps(["Come on,lets play together","Team performed well overall."]), "lang_code": "en" }).text