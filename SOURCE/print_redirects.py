'''

Testing Methods for redirecting scripts to log file

'''

from datetime import datetime




def printL(formatted_string, log_file, redirect_to_file):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if redirect_to_file:
        print(f"{current_time}: {formatted_string}", file=log_file)
    else:
        print(f"{current_time}: {formatted_string}")



def printT(formatted_string, log_file, redirect_to_file):
    if redirect_to_file:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{current_time}: {formatted_string}", file=log_file)
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(formatted_string)