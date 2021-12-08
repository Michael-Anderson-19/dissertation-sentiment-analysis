# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

import tensorflow as tf
import tensorflow_text as tf_text
import joblib 
import numpy as np
'''
    A class to wrap around a train deep learning model
    responsible for loading the trained model into memory and exposing it 
    to predictions 
    '''
class Model: 

    def __init__(self, model_path : str, label_path : str): 
        self.dl_model = None
        try: 
            
            self.load_model(model_path)
            self.load_labels(label_path)

        except Exception as err:
            raise Exception(f"An error occured while loading the model: {str(err)}")
    
    def make_single_prediction(self, input: str):
        return self.dl_model.predict(input)

    def predict(self, inputs):
        return self.dl_model.predict(inputs)
        
    def get_labels(self):
        return self.model_labels

    def get_label(self, index):
        return self.model_labels[index]

    def load_model(self, path: str):
        self.dl_model = tf.keras.models.load_model(path, compile=False)
    
    def load_labels(self, path : str):
        self.model_labels = joblib.load(path)



