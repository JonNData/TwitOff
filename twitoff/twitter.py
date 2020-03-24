# Retrieve tweets , ebedding, save into databse

import basilica
import tweepy
from decouple import config
from models import *

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                    config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), 
                                config('TWITTER_ACCESS_TOKEN'))
TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('BASILICA_KEY'))

# to do: add functions