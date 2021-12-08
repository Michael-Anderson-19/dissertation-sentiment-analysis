# author: Michael Anderson | student number: w18032122
# This work is part of the assessment for module KV6003 at Northumbria University

from response import Response 

class Prediction_Response(Response):
    """
    A class used the create the prediction response, extends the Response class 
    """
    def __init__(self, prediction : str, probability : str, tweets : dict, keyword : str): 
        super().__init__(status = 200, message="ok", prediction=prediction, probability=probability, tweets= tweets, error="", keyword=keyword )

    def get_response(self):
        return super().get_response()