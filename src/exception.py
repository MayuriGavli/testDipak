import sys
from src.logger import logging

def error_message_detail(error_msg,error_detail:sys):       #error_msg: This is a string that represents the actual error message , error_detail: sys: This expects the sys module
    _,_,exc_tb = error_detail.exc_info() #To retrieve the details of current exception = sys.exc_info() , first and second is type and value which is not required to us. 
    file_name = exc_tb.tb_frame.f_code.co_filename # Refers to the current stack frame where the exception occurred. f_code.co_filename: Retrieves the name of the file in which the error occurred.
    error_msg = f"Error script name {file_name} line number {exc_tb.tb_lineno} and error message {str(error_msg)} " # exc_tb.tb_lineno: Retrieves the line number in the file where the exception occurred.

    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_message_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg


if __name__ == "__main__" :

    try:
        i = 1/0
    except Exception as e:
        logging.info("can't divide by zero")
        raise CustomException(e,sys)


