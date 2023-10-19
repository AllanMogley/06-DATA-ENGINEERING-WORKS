import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3f3
import os
from dotenv import load_dotenv

access_key = os.getenv("API Key")
access_secret = os.getenv("API Key Secret")
consumer = os.getenv("Bearer Token")
consumer_key = os.getenv("Access Token")
consumer_secret = os.getenv("Access Token Secret")

# 