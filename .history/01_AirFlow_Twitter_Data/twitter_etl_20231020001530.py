import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv
load_dotenv()


# consumer = os.getenv("Bearer Token")
client = tweepy.Client(bearer_token='Bearer_Token')
# access_key = os.getenv("API_Key")
# access_secret = os.getenv("API_Key_Secret")
# consumer_key = os.getenv("Access_Token")
# consumer_secret = os.getenv("Access_Token_Secret")

# # Twitter Authentication
# auth = tweepy.OAuthHandler(access_key, access_secret)
# auth.set_access_token(consumer_key, consumer_secret)

# # Create an API object
# api = tweepy.API(auth)

# tweets = api.user_timeline(screen_name="@elonmusk", 
#                            count=20, 
#                            include_rts=False,
#                            tweet_mode="extended")

# print(tweets)   


# Replace with your own search query
query = 'from:@elonmusk -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)