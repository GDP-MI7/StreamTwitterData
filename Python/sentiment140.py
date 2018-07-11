from urllib.request import urlopen
import json
input = open("sample.txt", "r")
for i in input.readlines():
    # s = '{"data": [{"text": i}]}'
    b = bytes(i, 'utf-8')
    response = urlopen('http://www.sentiment140.com/api/bulkClassifyJson', b)
    page = response.read()
    print(page)