import tweepy
from pymongo import MongoClient
import csv
import json

#connecting to mongodb
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
tdb = client.twitter
htd = tdb.hashtagdata
print('connection successful')

#input twitter credentials
consumer_key = '*********'
consumer_secret = '*********'
access_token = '*********'
access_token_secret = '*********'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

# Get the User object for twitter...
#user = api.get_user(twitter)

#Taking input from he user
print('enter the hashtag')
hashtag = input()
print(hashtag)
print('enter date')
date = input()
print(date)
#collecting stream of tweets
for tweet in tweepy.Cursor(api.search,q = hashtag,count = 90000,lang="en",since = date).items():
    print (tweet.created_at, tweet.text)#adding tweets to the collection
    rec = {"user_screen_name": tweet.user.screen_name, "user_location": tweet.user.location, "created_at": tweet.created_at, "text": tweet.text, "hashtag": hashtag}
    htd.insert(rec)

'''
for tweet in tweepy.Cursor(api.search,q = hashtag,count = 90000,
                           lang="en",
                           since = '07/02/2018').items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
code to generate csv of tweets for hastag
# Open/Create a file to append data
csvFile = open(hashtag+'.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,q = hashtag,count = 9000,
                           lang="en",
                           since=date).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
'''