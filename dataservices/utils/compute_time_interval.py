
def initialize_log_file(os, sLogFile):

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


def calculate_time(sLogFile):

	import time
	import datetime
	from datetime import date
	from dateutil.relativedelta import relativedelta
	import queryDataServices

	f = open(sLogFile, "r+")
	strLog = f.read()

	# figure out how long it's been since the last query
	arLog = strLog.split(" ")
	strLastRan = arLog[3] + " " + arLog[4]
	dtNow = datetime.datetime.now()
	dtLastRan = datetime.datetime.strptime(strLastRan, "%Y-%m-%d %H:%M:%S.%f")
	dtDifference = relativedelta(dtNow, dtLastRan)
	iMinutes = dtDifference.minutes
	iHours = dtDifference.hours
	iDays = dtDifference.days
	iMonths = dtDifference.months
	iYears = dtDifference.years
	iTotMin = (iYears*525600)+(iMonths*43800)+(iDays*1440)+(iHours*60)+iMinutes

	print(str(dtNow) + ": checking last query time ...")
	print("  ... " + str(iTotMin) + " minutes since last webservices query (" + str(dtLastRan) + ")")

	f.close()

	return(iTotMin)
