# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

from prediction import Prediction


class Response:
    '''
    A base class to represent the json response returned by the api 
    '''
    def __init__(self, status:int, message:str, prediction:str, probability:str, tweets, error:str, keyword:str):
        self.status = status
        self.message = message
        self.prediction = prediction
        self.probability = probability
        self.tweets = tweets
        self.error = error
        self.keyword = keyword
    
    def get_response(self):

        response = dict()
        response['status'] = self.status
        response['message'] = self.message
        response['prediction'] = self.prediction
        response['probability'] = self.probability
        response['tweets'] = self.tweets
        response['error'] = self.error
        response['keyword'] = self.keyword

        return response 
