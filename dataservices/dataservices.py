#########################################################################################
# Update MicroStrategy cubes from webservices.
#   designed to run on a Developer machine, which is running periodically. For best 
#   results, run via batch script on user login.
#   Find new datasets here: https://data.cityofchicago.org/browse?limitTo=datasets
################################################################################JM,2019##

import sys
import os
import schedule
import time

import compute_time_interval

# iMinutesBetweenQueries is the number of minutes between Data Services queries (eg daily update = 1440 minutes)
iMinutesBetweenQueries = 1440
# iSecondsBetweenCheckElapsedTime is the number of seconds between checking the elapsed time
iSecondsBetweenCheckElapsedTime = 10 

loc = sys.path[0]
sLogFile = loc + "\\DataServices_log.txt"

print("DataServices scheduler has started.")

compute_time_interval.initialize_log_file(os, sLogFile)

schedule.every(iSecondsBetweenCheckElapsedTime).seconds.do(compute_time_interval.runlogging, loc, sLogFile, iMinutesBetweenQueries)

while True:
	schedule.run_pending()
	time.sleep(1)
