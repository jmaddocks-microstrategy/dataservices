
import os
import sys
import configparser
import schedule
import time
from dataservices.utils.logging import initialize


config = configparser.ConfigParser()
config.read("dataservices.cfg")

iQueryIntervalMinutes = int(config['SETTINGS']['queryintervalminutes'])
iCheckIntervalSeconds = int(config['SETTINGS']['checkintervalseconds'])

loc = sys.path[0]
sLogFile = loc + "\\DataServices_log.txt"

print("DataServices scheduler has started.")

initialize(os, sLogFile)

#schedule.every(iCheckIntervalSeconds).seconds.do(utils.compute_time_interval.runlogging, loc, sLogFile, iQueryIntervalMinutes)

while True:
    schedule.run_pending()
    time.sleep(1)
