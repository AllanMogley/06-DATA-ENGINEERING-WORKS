import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv

# access_key = os.getenv("API Key")
# access_secret = os.getenv("API Key Secret")
# # consumer = os.getenv("Bearer Token")
# consumer_key = os.getenv("Access Token")
# consumer_secret = os.getenv("Access Token Secret")

access_key = 'Q8MmdfLDZvTnm4qZOlr8dJhyM'
access_secret = 'LFVVzQihF0feCl3Jueo4AGYmoJU8OoyIbl5uiNjUNHfjWtXvJD'
# consumer = os.getenv("Bearer Token")
consumer_key = 800766681031114752-TJAlQfTSjNZ1W0bhj76tEspcMpqCYee
consumer_secret = rHeG7XE4tPkLLqx4kN9J4WV9JLsMAewrM73WSmSorqIEA

# API Key=Q8MmdfLDZvTnm4qZOlr8dJhyM
# API Key Secret=LFVVzQihF0feCl3Jueo4AGYmoJU8OoyIbl5uiNjUNHfjWtXvJD
# Bearer Token=AAAAAAAAAAAAAAAAAAAAAMVrqgEAAAAA5EWqCB3I7QWYlfe2qrxF2RFFmH4%3Dhn3bzogANCyV3bPxKQz1IRRveC9iso70zE0HINdEBhAiiXfllp
# Access Token=800766681031114752-TJAlQfTSjNZ1W0bhj76tEspcMpqCYee
# Access Token Secret=rHeG7XE4tPkLLqx4kN9J4WV9JLsMAewrM73WSmSorqIEA

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
