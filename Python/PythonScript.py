import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'HTNc6rm4tX63VYQKWQCV40TFm'
consumer_secret = 'bAWS75kNkDMKrWvGvzoGVYrRdjrtrZk7BaPwTBcBzdpfdHr0Il'
access_token = '969603656080330753-ucYDl5fW5aJmzT2AJIuR6wtKaa8Jf7A'
access_token_secret = 'HrI9XHNBqtQ0xxouDPqeY6OOOzLav1moLk1BgP7l29an9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
# csvFile = open('ua.csv', 'a')
#Use csv Writer
# csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=10,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
