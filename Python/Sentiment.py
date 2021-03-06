import re
import json
import tweepy
import json
import pymongo
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	'''
	Generic Twitter Class for sentiment analysis.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		# keys and tokens from the Twitter Dev Console
		consumer_key = 'WVQcbmO6MehpyWg5sN9AZG1Ea'
		consumer_secret = 'AKTauQTcluHM7nhf3t6CF0rbmgJL4pz8ViNiStq8JHu6rtUbxQ'
		access_token = '969591535254888449-jklQiG0CYsT2GRsD6xmXuDXP3pm7fh5'
		access_token_secret = 'xg2pC093ye6copEwLLoKufA3W0W8sXymOBmUa93q7y0D4'

		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			# set access token and secret
			self.auth.set_access_token(access_token, access_token_secret)
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		'''
		Utility function to clean tweet text by removing links, special characters
		using simple regex statements.
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		'''
		Utility function to classify sentiment of passed tweet
		using textblob's sentiment method
		'''
		# create TextBlob object of passed tweet text
		analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		# if analysis.sentiment.subjectivity > 0.5:

		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'
	
	def get_tweet_polarity(self, tweet):
		analysis = TextBlob(self.clean_tweet(tweet))
		return analysis.sentiment.polarity

	def get_tweet_subjectivity(self, tweet):
		analysis = TextBlob(self.clean_tweet(tweet))
		return analysis.sentiment.subjectivity

	# def get_tweet_createdat(self, tweet):
	# 	analysis = TextBlob(self.clean_tweet(tweet))
	# 	return tweet.created_at

	def get_tweets(self, query, count = 10):
		'''
		Main function to fetch tweets and parse them.
		'''
		# empty list to store parsed tweets
		tweets = []

		try:
			# call twitter api to fetch tweets
			fetched_tweets = self.api.search(q = query, count = count)

			# parsing tweets one by one
			for tweet in fetched_tweets:
				# empty dictionary to store required params of a tweet
				parsed_tweet = {}

				# saving text of tweet
				parsed_tweet['text'] = tweet.text
				# saving sentiment of tweet
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
				# saving polarity of tweet
				parsed_tweet['polarity'] = self.get_tweet_polarity(tweet.text)
				# saving subjectivity of tweet
				parsed_tweet['subjectivity'] = self.get_tweet_subjectivity(tweet.text)
				# saving date and time of tweet creation
				parsed_tweet['created_at'] = str(tweet.created_at)


				# appending parsed tweet to tweets list
				if tweet.retweet_count > 0:
					# if tweet has retweets, ensure that it is appended only once
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)

			# return parsed tweets
			return tweets

		except tweepy.TweepError as e:
			# print error (if any)
			print("Error : " + str(e))

print("Enter Hashtag:")
tag = input()
filename = tag + ".json"



def main():
	# creating object of TwitterClient Class
	api = TwitterClient()
	# calling function to get tweets
	tweets = api.get_tweets(query = 'tag', count = 10000)

	# writing all tweets to json file
	listtojson = json.dumps(tweets)
	loadingjson = json.loads(listtojson)
	# writing to a json file
	with open(filename, 'w') as outfile:
		json.dump(loadingjson, outfile)

	# inserting into mongodb
	connection = pymongo.MongoClient("mongodb+srv://gdp:gdp@socio-analyzer-8uxmb.mongodb.net/test?retryWrites=true")
	db=connection.final
	sentiment = db.final_collection
	sentiment.insert_many(loadingjson)


	# picking positive tweets from tweets
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	# percentage of positive tweets
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	# picking negative tweets from tweets
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	# percentage of negative tweets
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	# percentage of neutral tweets
		#	print("Neutral tweets percentage: {} % \
		#		".format(100*len(tweets - ntweets - ptweets)/len(tweets)))

	# printing first 5 positive tweets
	print("\n\nPositive tweets:")
	# s.write("\n\nPositive tweets:")
	for tweet in ptweets[:10]:
		print(tweet['text'])
		# s.write(tweet['text'])

	# printing first 5 negative tweets
	print("\n\nNegative tweets:")
	# s.write("\n\nNegative tweets:")
	for tweet in ntweets[:10]:
		print(tweet['text'])
		# s.write(tweet['text'])



if __name__ == "__main__":
	# calling main function
	main()