#extend response maybe 
from response import Response

class Error_Response(Response): 
    """
    A class used to create an error response, extends the Response class 
    """

    def __init__(self, error_status, error_message, error_details):

        super().__init__(status=error_status, message=error_message,prediction="", probability="",tweets = "", error = error_details, keyword = "")


    def get_response(self):

        return super().get_response()