import sys

def errorMessageDetails(error,error_detail:sys):
    '''
        exc_tb gives us which file and which particular line the error has occured
    '''
    _,_,exc_tb = error_detail.exc_info()
    error_message = f"Error occured in script {exc_tb.tb_frame.f_code.co_filename} in line number {exc_tb.tb_frame.f_lineno} with error message {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = errorMessageDetails(error=error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message