import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv
load_dotenv()


# consumer = os.getenv("Bearer Token")
# client = tweepy.Client(bearer_token='Bearer_Token')
access_key = os.getenv("API_Key")
access_secret = os.getenv("API_Key_Secret")
consumer_key = os.getenv("Access_Token")
consumer_secret = os.getenv("Access_Token_Secret")


# Twitter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="@elonmusk", 
                           count=20, 
                           include_rts=False)

tweets2 = api.get_follower_ids(screen_name="@elonmusk",
                            #    cursor, stringify_ids,
                               count = 20)

tweets3 = api.get_bookmarks()
# tweets = api.get_user(id=None, username="@elonmusk", expansions=None,
#                            tweet_fields=None, user_fields=None, user_auth=False)

print(tweets3)

print(api)