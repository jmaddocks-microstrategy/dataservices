
import os
import sys
import pathlib
import configparser
import schedule
import time
from dataservices.utils.logging import initialize
from dataservices.utils.timeIntervals import check_time_interval

loc = os.fspath(pathlib.Path(pathlib.Path(sys.path[0])))

config = configparser.ConfigParser()
config.read(loc+"dataservices.cfg")

i_query_interval_minutes = int(config['SETTINGS']['queryintervalminutes'])
i_check_interval_seconds = int(config['SETTINGS']['checkintervalseconds'])

s_log_file = loc + "DataServices_log.txt"
initialize(os, s_log_file)

print("DataServices scheduler has started.")

schedule.every(i_check_interval_seconds).seconds.do(check_time_interval, loc, s_log_file, i_query_interval_minutes)

while True:
    schedule.run_pending()
    time.sleep(1)
