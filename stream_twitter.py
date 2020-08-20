#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os,sys,re
import json
import config
import datetime
from textblob import TextBlob
from tweet_store import TweetStore


CONSUMER_KEY = config.twitter_api['consumer_key']
CONSUMER_SERECT = config.twitter_api['consumer_serect']
ACCESS_TOKEN = config.twitter_api['access_token']
ACCESS_SERECT = config.twitter_api['access_secret']

KEYWORDS = list(config.keyword)
store = TweetStore()

class MyStreamListener(tweepy.StreamListener):
    """
    This class inherits from tweepy.StreamListener to connect to Twitter Streaming API.
    """
    def on_connect(self):
        print('......Connected to Twitter Streaming API...... \n')


    def on_status(self, status):
        try:
            if ('RT @' not in status.text):
                blob = TextBlob(status.text)
                sent = blob.sentiment
                polarity = sent.polarity
                subjectivity = sent.subjectivity
                tweet_item = {
                    'id_str': status.id_str,
                    'text': status.text,
                    'polarity': polarity,
                    'subjectivity': subjectivity,
                    'username': status.user.screen_name,
                    'name': status.user.name,
                    'profile_image_url': status.user.profile_image_url,
                    'received_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                store.push(tweet_item)
                print('Push to redis:', tweet_item)
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
    print('......Collecting tweets contains keyword: {0}......'.format(' or '.join(key for key in KEYWORDS)))

    streamer.filter(track=KEYWORDS)


