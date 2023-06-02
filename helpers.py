import os
import time


def create_captures_dir(dir):
    if os.path.isdir(dir) is False:
        os.makedirs(dir)


def build_capture_output_name():
    return time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg'


def print_with_date(arg, date_format="%a %d %b %Y, %H:%M:%S"):
    print (time.strftime(date_format) + ": " + arg)
