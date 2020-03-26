import basilica
import tweepy
import os
from dotenv import load_dotenv
from twitoff.models import *

load_dotenv

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
basil_key = os.getenv("BASILICA_KEY")

TWITTER_AUTH = tweepy.OAuthHandler(
    consumer_key=consumer_key, consumer_secret=consumer_secret)
TWITTER_AUTH.set_access_token(access_token, access_token_secret)
TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(basil_key)
