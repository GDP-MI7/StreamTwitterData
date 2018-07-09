from textblob import TextBlob
input = open("sample.txt", "r")
for i in input.readlines():
    result = TextBlob(i)
    print(result.sentiment)
    if result.sentiment.polarity > 0:
        print("positive")
    elif result.sentiment.polarity == 0:
        print("neutral")
    else:
        print("negative")


# print(response)#         import requests
# # import json
# # input = open("sample.txt", "r")
# # for i in input.readlines():
# #     response = json.loads(requests.post("https://apis.paralleldots.com/v3/sentiment", text={ "api_key": "h1fPGh0H5LvtHU5LhaEnlhITrHLPSYNHbZTsyusz51s", "text": i, "lang_code": "en" }).text)
# #     