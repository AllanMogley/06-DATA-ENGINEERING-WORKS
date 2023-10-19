import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('API Key'))

access_key = os.getenv("API Key")
access_secret = os.getenv("API Key Secret")
# consumer = os.getenv("Bearer Token")
consumer_key = os.getenv("Access Token")
consumer_secret = os.getenv("Access Token Secret")

# Twitter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="@elonmusk", 
                           count=20, 
                           include_rts=False,
                           tweet_mode="extended")

print(tweets)   
