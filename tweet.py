import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'python'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('I liked this tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#for follower in tweepy.Cursor(api.followers).items():
#   follower.follow()
