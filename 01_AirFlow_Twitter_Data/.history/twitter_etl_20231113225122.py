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
    consumer_key="Q8MmdfLDZvTnm4qZOlr8dJhyM",
    consumer_secret="LFVVzQihF0feCl3Jueo4AGYmoJU8OoyIbl5uiNjUNHfjWtXvJD",
    access_token="800766681031114752-696Vq0jyMOhn3Vg7A9Ex3EUd1DEzzqO",
    access_token_secret=sqbz8kmpqSvz8miiDBKjUCVbswNJc7F7Iyh1509r0lBt5
)

# Twitter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
# api = tweepy.API(auth)

tweets = client.get_bookmarks()

print(tweets)

print(api)