#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:15:39 2020

@author: bingtian
"""

# import tweepy
import GetOldTweets3 as got

# consumer_key = 'TqZ2BpcyIb6i4B34fQRcASbap'
# consumer_secret = 'KLJHp6eiE5hGnkjBIX2KgeHKdq5RQ15lqKiYGMskh8XxYpNGw8'
# access_token = '171131845-f4srxVm54xppbTw29sCBJrVuhzelFpAcdhA6DsFj'
# access_secret = 'eV5LXg2MM3IfkHxFv4ucRErfeHd28inaopselAHfOn8In'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)

# number_of_tweets = 200

# public_tweets = api.search('uchicago', count=100)
# for tweet in public_tweets:
#     print(tweet.text)
    
    
text_query = 'uchicago'
count = 200
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                            .setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]

for date, text in text_tweets:
    print(date)
    print(text)
    print("\n")
    
    