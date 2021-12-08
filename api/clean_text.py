# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

import re

class Text_Cleaner:

    '''
    This class creates a set of methods for preprocessing text ready for use with the sentiment analysis model
    '''

    def __init__(self):

        #define the emoji dictionary with corresponding sentiment
        self.emoji_dict = {'😂':'positive','❤️':'positive','😍':'positive',
						'🤣':'positive', '😊':'positive','💕':'positive',
						'😭':'negative','😘':'positive','👍':'positive',
						'😅':'negative','👏':'positive','😁':'positive',
						'🔥':'positive','💔':'negative','💖':'positive',
						'😢':'negative','🤔':'negative','😆':'positive',
						'🙄':'negative','😉':'positive','👌' :'positive',
						'🤗':'positive','😔':'negative','😎':'positive',
						'😇':'positive','🤦':'negatvie','🎉':'positive',
						'💞':'positive','✌️':'positive','✨':'positive',
						'😱':'negative','😌':'positive','🙌':'positive',
						'😋':'positive','😏':'positive','🙂':'positive',
						'🤩':'positive','😄':'positive','😀':'positive',
						'😃':'positive','💯':'positive','🙈':'negative',
						'🤭':'positive','❣️':'positive','😜':'positive',
						'💋':'positive','😪':'negative','😑':'negative',
						'😞':'negative','😩':'negative','😡':'negative',
						'🤪':'positive','😥':'negative','🤤':'positive',
						'😳':'positive','😚':'positive','😝':'positive',
						'😴':'negative','😬':'negative','🙃':'negative',
                        '😻':'positive','😓':'negative','😣':'negative',
                        '☹️':'negative','🎊':'positive','💘':'positive',
                        '😠':'negative','☝️':'negative','😕':'negative',
                        '😒':'negative'}
                        
    #function to remove the contractions between words		
    def remove_contractions(self,tweet):
        #remove won't and replace with will not
        tweet = re.sub(r"won't", "will not",tweet)
        #remove can't and replace with can not
        tweet = re.sub(r"can't", "can not",tweet)
        #remove 's from words and replace with is,  as in it's = it is
        tweet = re.sub(r"\'s", " is",tweet)
        #remove 'd from words and replace with would, as in I'd = I would
        tweet = re.sub(r"\'d", " would",tweet)
        #remove n't from words and replace with not, as in wouldn't = would not
        tweet = re.sub(r"n\'t", " not",tweet)
        #remove 're from words and replace with, are as in you're = you are
        tweet = re.sub(r"\'re", " are",tweet)
        #remove 'll from words and replace with will, as in I'll = I will
        tweet = re.sub(r"\'ll", " will",tweet)
        #remove 't from words and replace with not
        tweet = re.sub(r"\'t", " not",tweet)
        #remove 've from words and replace with have, as in could've = could have
        tweet = re.sub(r"\'ve", " have",tweet)
        #remove 'm from words and replace with am, as in I'm = I am
        tweet = re.sub(r"\'m", " am",tweet)
        #return the uncontracted sentence
        return tweet

    #function to remove user handles from text such as @user, this will remove the full handle including the text
    def remove_user_handles(self, tweet):
        tweet = re.sub(r"@[^\s]+", "", tweet)
        return tweet

     #function to remove all special symbols from the sentence
    def remove_symbols(self,tweet):
        tweet = re.sub("\S*\d\S*", "", tweet).strip()
        return tweet

     #function to remove numbers from text     
    def remove_numbers(self,tweet):
        #remove all characters except A-Z/a-z
        tweet = re.sub('[^A-Za-z]+', ' ', tweet)
        return tweet

    #function to replace an emoji its sentiment
    def emoji_lookup(self, tweet):
        if tweet in self.emoji_dict:
            return self.emoji_dict[tweet]
        else:
            return tweet

    #function to remove any urls in the text
    def remove_URL(self,tweet):
        tweet = re.sub(r"http\S+", "", tweet)
        return  re.sub(r"www\.\S+", "", tweet)
    
    #function to remove apply all pre-processing steps in the correct order
    def clean_tweet(self, tweet, return_string = False):
        
        #remove contractions
        tweet = self.remove_contractions(tweet)
        #remove any white space 
        tweet = tweet.strip()
        #remove user handles from the tweet
        tweet = self.remove_user_handles(tweet)
        #make all text lowercase
        tweet = tweet.lower()
        #split the text into individual tokens based on whitespace 
        tokens = tweet.split()
        #empty list to hold all tokens after cleaning
        new_tweet = []
        #iterate through each token in the text 
        for token in tokens:

            #remove any urls
            token = self.remove_URL(token)

            #replace emojis with their sentiment
            token = self.emoji_lookup(token)

            #remove symbols
            token = self.remove_symbols(token)
            
            #remove noumbers
            token = self.remove_numbers(token)
            
            #remove whitespace
            token = token.strip()

            #if token is empty skip to next token and don't append
            if(token == ""):
                continue
            #append token to list
            new_tweet.append(token)
                        
        if return_string == True:
            #optionally concatinate all tokens into a string
            new_tweet = " ".join(new_tweet)
            
        return new_tweet


