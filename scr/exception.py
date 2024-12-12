import sys

def error_message_detail(error_msg,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.exc_frame.


