#!/usr/bin/env python


import django
import os
import sys
import time
import tweepy

from random import choice, seed

sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog.settings'

django.setup()

from blog.models import Article, Tweet  # noqa E402


SEND_TWEET = False

article_uri = 'http://harlinseritt.com/blog/article'

TYPE_ARTICLE = 'article'
TYPE_TWEET = 'tweet'
DEFAULT_TYPE = TYPE_ARTICLE
TW_CONSUMER_KEY = os.environ['TW_CONSUMER_KEY']
TW_CONSUMER_SECRET = os.environ['TW_CONSUMER_SECRET']
TW_ACCESS_TOK = os.environ['TW_ACCESS_TOK']
TW_TOK_SECRET = os.environ['TW_TOK_SECRET']


class Tweeter:

    def __init__(self, post_type=TYPE_ARTICLE):
        seed(time.time())
        self.post_type = post_type

    def _get_article_msg(self):
        article_list = Article.objects.filter(
            is_published=True, tweet_article=True
        )
        article = choice(article_list)
        return f'{article.title} - {article_uri}/{article.slugged_title}'

    def _get_tweet_msg(self):
        tweet_list = Tweet.objects.filter(is_enabled=True)
        tweet = choice(tweet_list)
        return tweet.message

    def _get_msg(self):
        if self.post_type.lower() == TYPE_ARTICLE:
            return self._get_article_msg()
        elif self.post_type.lower() == TYPE_TWEET:
            return self._get_tweet_msg()

    def _get_api(self):
        auth = tweepy.OAuthHandler(
            TW_CONSUMER_KEY,
            TW_CONSUMER_SECRET
        )
        auth.set_access_token(
            TW_ACCESS_TOK,
            TW_TOK_SECRET
        )
        return tweepy.API(auth)

    def run(self):
        msg = self._get_msg()
        api = self._get_api()
        print(msg)
        if SEND_TWEET:
            api.update_status(msg)


if __name__ == '__main__':
    try:
        post_type = sys.argv[1]
    except IndexError:
        post_type = DEFAULT_TYPE

    tweeter = Tweeter(post_type)
    tweeter.run()
