import paralleldots
input = open("sample.txt", "r")
for i in input.readlines():
    print(sentiment(i))