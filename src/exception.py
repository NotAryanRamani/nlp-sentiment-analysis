import sys


def except_msg_details(except_msg, except_detail: sys):
    _, _, except_tb = except_detail.exc_info()
    filename = except_tb.tb_frame.f_code.co_filename
    linenumber = except_tb.tb_lineno
    except_msg = ' Exception Occured: Script Name: {0}, Line: {1}, Exception Message: {2}'.format(
        filename, 
        linenumber,
        str(except_msg)
        )
    return except_msg


class CustomException(Exception):
    def __init__(self, except_msg, except_detail: sys):
        self.except_msg = except_msg_details(except_msg, except_detail=except_detail)
        super().__init__(except_msg)
        
    def __str__(self):
        return self.except_msg