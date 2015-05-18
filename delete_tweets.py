#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import requests
from requests_oauthlib import OAuth1
from datetime import date, datetime, timedelta
from time import sleep

from auth import *

auth = OAuth1(consumer_key, consumer_secret,
              access_token, access_token_secret)

### SETTINGS ###

screen_name = 'cmerrill'

# Time between delete requests, in seconds
# Minimum value is 5 in order to keep within Twitter API rate limits
rate_delay = 6  

# Maximum age, in days, of tweets to keep
max_age_in_days = 30

# Minimum number of tweets to keep, regardless of age
min_tweets_to_keep = 10

# IDs of specific Tweets to keep
protected_tweets = [600437773242359808, ]


timeline_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s&count=200" % (screen_name,)

max_age = date.today() - timedelta(days=max_age_in_days)

timeline = requests.get(timeline_url, auth=auth)

if timeline.status_code == 200:
    
    tweets = json.loads(timeline.text)

    if len(tweets) > min_tweets_to_keep:

        for t in tweets[min_tweets_to_keep:]:
            tweet_id = t['id']
            tweet_creation = datetime.strptime(t['created_at'], '%a %b %d %X %z %Y')
            tweet_date = date(tweet_creation.year, tweet_creation.month, tweet_creation.day)
            
            if tweet_date < max_age and tweet_id not in protected_tweets:

                delete_tweet_url = "https://api.twitter.com/1.1/statuses/destroy/%s.json" % (tweet_id,)
            
                requests.post(delete_tweet_url, auth=auth)

                sleep(rate_delay)
