
import os
import sys
import configparser
import schedule
import time
from dataservices.utils.logging import initialize
from dataservices.utils.time_intervals import calculate_time

config = configparser.ConfigParser()
config.read("dataservices.cfg")

iQueryIntervalMinutes = int(config['SETTINGS']['queryintervalminutes'])
iCheckIntervalSeconds = int(config['SETTINGS']['checkintervalseconds'])

loc = sys.path[0]
sLogFile = loc + "\\DataServices_log.txt"

print("DataServices scheduler has started.")

initialize(os, sLogFile)

schedule.every(iCheckIntervalSeconds).seconds.do(calculate_time, loc, sLogFile, iQueryIntervalMinutes)

while True:
    schedule.run_pending()
    time.sleep(1)
