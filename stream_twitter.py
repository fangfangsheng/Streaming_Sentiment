#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os,sys,re
import json
from pymongo import MongoClient
import config
import datetime


CONSUMER_KEY = config.twitter_api['consumer_key']
CONSUMER_SERECT = config.twitter_api['consumer_serect']
ACCESS_TOKEN = config.twitter_api['access_token']
ACCESS_SERECT = config.twitter_api['access_secret']
MONGO_HOST = config.host
KEYWORD = list(config.keyword)

def mongodb_store(created_at, text, tweet_id, user_id, user_name, follwers_num, tweet_lang, country):
    client = MongoClient(MONGO_HOST)
    db = client.mydatabase
    data_mongo = {}
    data_mongo['id_str'] = tweet_id
    data_mongo['user_name'] = user_name
    data_mongo['user_id'] = user_id
    data_mongo['tweeted_at'] = created_at
    data_mongo['text'] = text
    data_mongo['num_follower'] = follwers_num
    data_mongo['country'] = country
    data_mongo['lang'] = tweet_lang
    # insert data in collection
    db.tweet_collect.insert_one(data_mongo)

class MyStreamListener(tweepy.StreamListener):
    """
    This class inherits from tweepy.StreamListener to connect to Twitter Streaming API.
    """
    def on_connect(self):
        print('......Connected to Twitter Streaming API...... \n')


    def on_status(self, status):
        try:
            if status.retweeted == False:
                try:
                    text = status.extended_tweet['full_text']
                except AttributeError:
                    text = status.text
                created_at = status.created_at
                tweet_id = status.id_str
                user_id = status.user.id_str
                user_name = status.user.name
                follwers_num = status.user.followers_count
                tweet_lang = status.lang
                country = status.place.country if status.place else ''
                mongodb_store(created_at, text, tweet_id, user_id, user_name, follwers_num, tweet_lang, country)
        except Exception as e:
            print(e)

    def on_error(self, status_code):
        if status_code == 420:  # returning False in on_data disconnects the stream
            return False
        else:  # continue listening if other errors occur
            print('An Error has occurred: ' + repr(status_code))
            return True


if __name__ == '__main__':
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SERECT)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SERECT)
    api = tweepy.API(wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    listener = MyStreamListener(api=api)
    streamer = tweepy.Stream(auth=auth, listener=listener, tweet_mode='extended')
    print('......Collecting tweets contains keyword: {0}......'.format(' or '.join(key for key in KEYWORD)))

    streamer.filter(track=KEYWORD)


