
import os
import sys
import configparser
import schedule
import time
from dataservices.utils.logging import initialize
from dataservices.utils.timeIntervals import check_time_interval

config = configparser.ConfigParser()
config.read("dataservices.cfg")

i_query_interval_minutes = int(config['SETTINGS']['queryintervalminutes'])
i_check_interval_seconds = int(config['SETTINGS']['checkintervalseconds'])

loc = sys.path[0]
s_log_file = loc + "\\DataServices_log.txt"
initialize(os, s_log_file)

print("DataServices scheduler has started.")

schedule.every(i_check_interval_seconds).seconds.do(check_time_interval, loc, s_log_file, i_query_interval_minutes)

while True:
    schedule.run_pending()
    time.sleep(1)
