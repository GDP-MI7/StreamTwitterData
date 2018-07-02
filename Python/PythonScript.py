import tweepy
from pymongo import MongoClient
import csv
import json
import pandas as pd


#connecting to mongodb
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
tdb = client.twitter
htd = tdb.hashtagdata
tdb.htd.ensure_index("id", unique=True, dropDups=True)
print('connection successful')

####input your credentials here
consumer_key = 'cUl8PhvD2GBmBU7Oyu1yHcSzZ'
consumer_secret = 'KE2BoICmlSaNr75VWZtlXL5eIjLyRYR7hdBfVHwNAUd0P3PyFc'
access_token = '1008783848812023812-KkImFZ0o41ie8troJgwciwqLSSYfuw'
access_token_secret = 'qWoTlhuXronTzCdDdTmPOoLK0tr2oRHu9P3uoR0somtJk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=False)

#Taking input from he user
print('enter the hashtag')
hashtag = input()
print(hashtag)
print('enter date')
date = input()
print(date)
for tweet in tweepy.Cursor(api.search,q = hashtag,count = 9000,
                           lang="en",
                           since=date).items():
    #adding in the database
    rec = {"created_at": tweet.created_at,
                           "text": tweet.text}
    # inserting the data in the database
    htd.insert(rec)
    #print (tweet.created_at, tweet.text)

'''
old code
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