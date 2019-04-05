
def initialize(os, sLogFile):

        if os.path.isfile(sLogFile):
                print("log file exists")
        else :
                print("creating log file")
                f = open(sLogFile, "w+")
                f.write("created file on: 2000-01-01 01:01:01.0000")
                f.close()

def runlogging(loc, sLogFile, iMinutesBetweenQueries):

	import time
	import datetime
	import queryDataServices

	f = open(sLogFile, "r+")

	if calculate_time(sLogFile)>=iMinutesBetweenQueries :
		print("  will query webservices now")
		f.seek(0)
		f.write("queried data at: " + str(datetime.datetime.now()))
		f.truncate()
		queryDataServices.getServices(str(loc))

	else :
		print("  will not query webservices at this time")
	f.close()