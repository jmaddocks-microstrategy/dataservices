
def get_loc():
    import os
    import sys
    import pathlib

    return os.fspath(pathlib.Path(pathlib.Path(sys.path[0]))) + "/"


def get_config():
    import configparser
    config = configparser.ConfigParser()
    config.read(get_loc() + "dataservices.cfg")
    return config


def log_file_name():

    return "data_services_log.txt"


def get_log_file(open_type):

    s_log_file = get_loc() + log_file_name()

    if open_type == "w":
        log_file = open(s_log_file, "w+")
    else:
        log_file = open(s_log_file, "r+")

    return log_file


def initialize_log_file():
    import os

    s_log_file = get_loc() + log_file_name()

    if os.path.isfile(s_log_file):
        print("log file exists")
    else :
        print("creating log file")
        f = open(s_log_file, "w+")
        f.write("created file on: 2000-01-01 01:01:01.0000")  # set the last write time to 10 years ago so that the first run triggers update
        f.close()

