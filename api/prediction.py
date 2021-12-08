# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

import numpy as np

class Prediction: 
    '''
    controller class for managing the predictions made on tweets 
    '''
    def __init__(self, dl_model):
        self.dl_model = dl_model

        self.positive = 0
        self.negtaive = 0 

    def set_data(self, data):
        self.data = data

    def predict_data(self):
        self.predictions = self.dl_model.predict(self.data)

    def format_average_predictions(self):
        summed_positive = 0.0
        summed_negative = 0.0

        for pred in self.predictions:

            summed_positive += pred[0]
            summed_negative += pred[1]

        #workout the average for each class
        average_positive_sentiment = summed_positive/len(self.predictions)*100
        average_negative_sentiment = summed_negative/len(self.predictions)*100

        #get the average class label
        average_label = self.get_max_label([summed_positive, summed_negative])

        #combine the average probabilities into a string
        average_probability_string = f"{average_positive_sentiment:.2f}% {self.dl_model.get_label(0)} and {average_negative_sentiment:.2f}% {self.dl_model.get_label(1)}"
 
        return [average_label, average_probability_string]


    def get_max_label(self,labels):

        max_label = self.dl_model.get_label(np.argmax(labels))
        return max_label

    def format_individual_tweet_Prediction(self, clean_tweets : dict): 

        tweet_predictions = list()

        for pred, twt in zip(self.predictions, clean_tweets):

            tweet = dict() 
            tweet['text'] = twt
            positve_probability = pred[0]*100
            negative_probability = pred[1]*100
            tweet_prediction = self.get_max_label(pred) 
            tweet_probability = f"{positve_probability:.2f}% {self.dl_model.get_label(0)}, {negative_probability:.2f}% {self.dl_model.get_label(1)}"
            tweet['prediction'] = tweet_prediction
            tweet['probability'] = tweet_probability  
            tweet_predictions.append(tweet)   

        return tweet_predictions
         