# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)

from flask import Flask, jsonify, request
from flask_cors import CORS

from clean_text import Text_Cleaner 
from collect_tweets import Tweet_Collecter 
from model import Model
from prediction import Prediction 
from prediction_response import Prediction_Response
from error_response import Error_Response

#create flask app 
app = Flask(__name__)
#set CORS to allow cross-origin resource sharing
cors = CORS(app)

print("\nserver starting....\n")

#path to the serialised labels and trained model
label_path = './saved_model/labels.p'
model_path = './saved_model/bertCNN2'

#load the serialised model and initialise the model class 
try: 
    model = Model(model_path=model_path, label_path=label_path)
except Exception as err:
    print(str(err))


print("\nloading neural network....\n")

#create instance of the TextCleaner class for performing text pre-processing
preprocessor = Text_Cleaner()

#create instance of TweetCollector to collect tweets from the API - takes TextCleaner object to preprocess tweets as they are collected
twitter_API = Tweet_Collecter(preprocessor)

#define the endpoint for recieving requests, collecting tweets and making predictions
@app.route('/predict/tweets', methods=['POST','GET'])
def predict_tweets():

    keyword = ""

    #collect keyword from request
    if request.method == "GET":
        keyword = request.args.get('text')
    
    elif request.method == "POST": 
        request_data = request.json
        keyword = request_data['text']
    
    if keyword.strip() != "":
        try:
            response_controller = Prediction(model)
            
            
            clean_tweets, raw_tweets = twitter_API.get_tweets(keyword)
            response_controller.set_data(clean_tweets)
            response_controller.predict_data()
            avg_pred, avg_prob = response_controller.format_average_predictions()
            predicted_tweets = response_controller.format_individual_tweet_Prediction(raw_tweets)
            response = Prediction_Response(avg_pred,avg_prob, predicted_tweets, keyword)

        except Exception as err:

            response = Error_Response(500,"Internal server error", f"An internal error has occured: {str(err)}")
        
    else:
        response = Error_Response(400,"Bad Request", "Empty text field recieved, text field must not be empty")

    return jsonify( response.get_response() )

if __name__ == "__main__":
    app.run()#debug=True)
