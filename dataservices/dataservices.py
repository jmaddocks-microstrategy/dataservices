
import os
import sys
import configparser
import schedule
import datetime

#import compute_time_interval


config = configparser.ConfigParser()
config.read("dataservcies.cnf")

iMinutesBetweenQueries = int(config.get('SETTINGS', 'MINUTESBETWEENQUERIES'))
iSecondsBetweenCheckElapsedTime = int(config.get('SETTINGS', 'SECONDSBETWEENCHECKELAPSEDTIME'))

loc = sys.path[0]
sLogFile = loc + "\\DataServices_log.txt"

print("DataServices scheduler has started.")

utils.compute_time_interval.initialize_log_file(os, sLogFile)

schedule.every(iSecondsBetweenCheckElapsedTime).seconds.do(utils.compute_time_interval.runlogging, loc, sLogFile, iMinutesBetweenQueries)

while True:
	schedule.run_pending()
	time.sleep(1)
