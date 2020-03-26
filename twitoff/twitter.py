import basilica
import tweepy
import os
from dotenv import load_dotenv
from .models import User, Tweet, DB

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BASILICA = basilica.Connection(os.getenv("BASILICA_KEY")

twit = tweepy.OAuthHandler(consumer_key, consumer_secret)
twit.set_access_token(access_token, access_token_secret)
TWITTER = tweepy.API(twit)

# def twitter_api_client():

#     TWITTER_AUTH = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     TWITTER_AUTH.set_access_token(access_token, access_token_secret)
#     TWITTER = tweepy.API(TWITTER_AUTH)

# BASILICA = basilica.Connection(config('BASILICA_KEY'))

# to do: add functions
