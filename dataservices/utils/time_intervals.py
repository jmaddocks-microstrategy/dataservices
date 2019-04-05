


def calculate_time(sLogFile):

	# import time
	import datetime
	# from datetime import date
	from dateutil.relativedelta import relativedelta
    # from datservices.utils.queryDataServices import queryDataServices

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
