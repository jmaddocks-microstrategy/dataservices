
def initialize(os, s_log_file):

        if os.path.isfile(s_log_file):
                print("log file exists")
        else :
                print("creating log file")
                f = open(s_log_file, "w+")
                f.write("created file on: 2000-01-01 01:01:01.0000")
                f.close()

