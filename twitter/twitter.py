import tweepy
from tweepy.auth import OAuthHandler
from twitter.models import Tweet
from datetime import date , datetime

def my_user_tweets():
    auth = OAuthHandler('fFXyrFTCI0LRqOinwStdmVNT0','ucE1sQPtjouJKlP3TzUXTv1ib9AJVrvoltt7yz3rjU67xSGJkL')
    auth.set_access_token('1091673443433627648-AZhLdT4T7q2gXDv7OIusYb4P7t07Gg','Rv4d0OUPfO4Cz9vEdVdiPTYUlep59MRMP050RjDDEu9GZ')
    api = tweepy.API(auth)
    user_tweets = api.user_timeline()
    for user_tweet in user_tweets:
        user_tweet = Tweet(tweet_text= user_tweet.text, published_date=user_tweet.created_at)
        user_tweet.save()
    return print('successfully')

def search_tweets(twitter_user=None, num_of_tweets=1):
    auth = OAuthHandler('fFXyrFTCI0LRqOinwStdmVNT0','ucE1sQPtjouJKlP3TzUXTv1ib9AJVrvoltt7yz3rjU67xSGJkL')
    auth.set_access_token('1091673443433627648-AZhLdT4T7q2gXDv7OIusYb4P7t07Gg','Rv4d0OUPfO4Cz9vEdVdiPTYUlep59MRMP050RjDDEu9GZ')
    api = tweepy.API(auth)
    user_tweets = api.user_timeline(count=num_of_tweets, id=twitter_user,tweet_mode='extended')
    return user_tweets

        





















# class MyStreamListener(tweepy.StreamListener):

#         def on_status(self, data):
#                 print(data)

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = user_tweets().api.auth, listener=myStreamListener)

# myStream.filter(track=['python'])