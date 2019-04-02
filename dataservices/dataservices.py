
# iMinutesBetweenQueries is the number of minutes between Data Services queries (eg daily update = 1440 minutes)
iMinutesBetweenQueries = int(os.environ['MINUTESBETWEENQUERIES'])
# iSecondsBetweenCheckElapsedTime is the number of seconds between checking the elapsed time
iSecondsBetweenCheckElapsedTime = int(os.environ['SECONDSBETWEENCHECKELAPSEDTIME'])

loc = sys.path[0]
sLogFile = loc + "\\DataServices_log.txt"

print("DataServices scheduler has started.")

compute_time_interval.initialize_log_file(os, sLogFile)

schedule.every(iSecondsBetweenCheckElapsedTime).seconds.do(compute_time_interval.runlogging, loc, sLogFile, iMinutesBetweenQueries)

while True:
	schedule.run_pending()
	time.sleep(1)
