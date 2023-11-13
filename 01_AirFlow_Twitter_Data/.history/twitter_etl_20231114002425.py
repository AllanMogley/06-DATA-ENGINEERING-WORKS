import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv
load_dotenv()

# Twitter API Credentials
access_key = os.getenv("API_Key")
access_secret = os.getenv("API_Key_Secret")
consumer_key = os.getenv("Access_Token")
consumer_secret = os.getenv("Access_Token_Secret")

client = tweepy.Client(
    consumer_key='PkKlNqXIh5EseHFFzxHqNpFVL',
    consumer_secretAPI_Key_Secret=p2to10bhk5bebhaVNXhHhYi9cwXxgNS9xJP7Wb6BMycc0zZy5P,
    access_token=consumer_key,
    access_token_secret=consumer_secret
)


tweets = client.get_user(username = "Twitter Dev")
# print(tweets)