# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:31:56 2020
@author: Devesh Waingankar
Python Version: 3.6 or above
"""
import tweepy
import json
import pymongo
from pymongo import MongoClient
import dns
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# twitter credentials
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            mongo_client = pymongo.MongoClient("mongodb+srv://rest of your link")
            db = mongo_client['twitter']
            collection = db.mytweets
            tweets = json.loads(data)
            collection.insert(tweets)
            return True
        except Exception as e:
            print (e)
            exit()

    def on_error(self, status):
        print(status)
        exit()

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    stream = Stream(auth, listener)
    list = ['Modi', 'JNU', 'AZADI', 'Delhi']
    stream.filter(track=list, is_async=True)  # is_async=True to terminate the connection
