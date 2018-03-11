import tweepy
from  textblob import TextBlob

consumer_key = "d8hrV8lJ4dqWYo8ETgnKk4IyH"
consumer_secret = "p7W6xokNficSVlAH6chT0qMHecESQ0xWGk52JQYJ7k8PbgwHdg"

access_token = "4558143982-1JjmQtKk5czYz90UPtubsOCdwrlGuwueiXHfyuU"
access_token_secret = "3xxdSTF5MhHS3d3HvC3gt4dTX1lCHdK7og4GkOgo0aoaY"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
