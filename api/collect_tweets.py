# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

from credentials import get_credentials
import tweepy

class Tweet_Collecter:
    """
    This class connects to the twitter api and collects tweets containing the specified keyword or phrase
    """
    
    def __init__(self, Text_cleaner):
        #dependency injection of the TextCleaner object
        self.prepro = Text_cleaner
        
        #import twitter api credentials 
        API_KEY, SECRET = get_credentials()

        #create authentication handler 
        auth = tweepy.AppAuthHandler(API_KEY, SECRET)

        #creaete an twitter api connection
        self.api = tweepy.API(auth) 
    
    def get_tweets(self,keyword):
        num_tweets = 25
        clean_tweets = []
        raw_tweets = []
        try:
            for tweet in tweepy.Cursor(self.api.search, q=keyword +'-filter:retweets',
                                       lang='en', tweet_mode='extended', count=num_tweets).items(num_tweets):
                #append the raw uncleaned text to a list    
                raw_tweets.append(tweet.full_text)
                #preprocess the tweet and add to the clean_tweets list
                clean_tweets.append(self.prepro.clean_tweet(tweet.full_text, return_string = True))
                #return both lists
        except:
            raise Exception("Twitter API request limit reached")
        return [clean_tweets, raw_tweets]


