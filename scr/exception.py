import sys

def error_message_detail(error_msg,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.exc_frame.f_code.co_file_name
    error_msg = f"Error script name {file_name} line number {exc_tb.tb_lineno} and error message {str(error_msg)} "

    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super.__init__(error_msg)
        self.error_msg = error_message_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg





