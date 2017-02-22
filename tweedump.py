#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from sauce import *

def get_tweet_set(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=10)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	#oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab

	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [['@', screen_name, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('tweets.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	users = ['ezraklein', 'buzzfeedben', 'daveweigel', 'nprpolitics', 'mcclatchydc',
	'senateus', 'annakendrick47', 'vancityreynolds', 'kanyewest', 'adamschefter',
	'iainmacintosh', 'dougferguson405']
	for user in users:
		print(user)
		get_tweet_set(user)

