import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv
load_dotenv()

# Twitter API Credentials
consumer_key = os.getenv("Access_Token")
consumer_secret = os.getenv("Access_Token_Secret")
access_key = os.getenv("API_Key")
access_secret = os.getenv("API_Key_Secret")

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token="Access Token here",
    access_token_secret="Access Token Secret here"
)

# Twitter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
api = tweepy.API(auth)

tweets = api.get_bookmarks()

print(tweets)

print(api)