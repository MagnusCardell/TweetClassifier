#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from sauce import * #file with personal credentials for using API

def get_tweets(genre, filename):
	#Twitter only allows access to a users most recent 3240 tweets
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	print(genre)


	for user in genre:
		print(user)
		alltweets = []
		new_tweets = api.user_timeline(screen_name = user,count=5)
		alltweets.extend(new_tweets)

		#transform the tweepy tweets into a 2D array that will populate the csv	
		outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
		#write the csv, append	
		with open(filename+'.csv', 'a') as f:
			writer = csv.writer(f)
			writer.writerows(outtweets)
	
		#pass


if __name__ == '__main__':
	#pass in the username of the account you want to download

	sports = ['adamschefter', 'iainmacintosh', 'dougferguson405']
	news = ['nprpolitics', 'mcclatchydc', 'senateus']
	celebs = ['annakendrick47', 'vancityreynolds', 'kanyewest']
	politics = ['ezraklein', 'buzzfeedben', 'daveweigel']

	get_tweets(news, 'news')
	get_tweets(politics, 'politics')
	get_tweets(celebs, 'celebs')
	get_tweets(sports, 'sports')

	# users = ['ezraklein', 'buzzfeedben', 'daveweigel', 'nprpolitics', 'mcclatchydc',
	# 'senateus', 'annakendrick47', 'vancityreynolds', 'kanyewest', 'adamschefter',
	# 'iainmacintosh', 'dougferguson405']
	# for user in users:
	# 	print(user)
	# 	get_tweets(user)

