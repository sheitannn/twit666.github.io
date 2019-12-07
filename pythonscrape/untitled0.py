#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)

consumer_key = info['CONSUMER_KEY']
consumer_secret = info['CONSUMER_SECRET']
access_token = info['ACCESS_KEY']
access_token_secret = info['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


hashtag = "climate"

csvFile = open(hashtag+".csv", "a")
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#"+hashtag,count=200, lang="en", since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
