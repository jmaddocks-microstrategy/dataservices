
def getServices(loc):

	import pandas as pd
	from pandas import ExcelWriter
	from pandas import ExcelFile
	import xlrd

	df = pd.read_excel(loc+"\\DataServices_List.xlsx", sheet_name="Sheet1")

	for i in range(0, len(df)):
		arThisService = df.iloc[i]
		updateCube(arThisService)

def updateCube(arThisService):

	strTableName = arThisService[0]
	strURL = arThisService[1]
	strAppToken = arThisService[2]
	strUserName = arThisService[3]
	strPassword = arThisService[4]
	strWebserviceID = arThisService[5]
	strDateField = arThisService[6]
	iMonthsOfData = int(arThisService[7])
	strCubeID = arThisService[8]

	import pandas as pd
	from sodapy import Socrata
	import datetime
	from datetime import date
	from dateutil.relativedelta import relativedelta

	dtStartDate = date.today() + relativedelta(months=-1*iMonthsOfData)

	client = Socrata(strURL,
					strAppToken, 
					username=strUserName, 
					password=strPassword
					)

	print("	" + strTableName + " query started at: " + str(datetime.datetime.now()))

	strDataQuery = strDateField + " > '" + str(dtStartDate) + "T00:00:00.000'"
	#strDataQuery = strDateField + " between '2018-07-17T00:00:00.000' and '2019-03-02T23:59:59.000'"

	print("	  using query: '" + strDataQuery + "'")
	results = client.get(strWebserviceID, where=strDataQuery, limit=99999999)
	client.close()

	# Convert results to pandas DataFrame
	df = pd.DataFrame.from_records(results)
	if len(df.index) > 0:

		# convert series to the correct types
		# right now mstrio does not import datetime values ... so use this formula in Mstr to create a new datetime attribute: ToDateTime(LeftStr(date@ID, 10))
		# df[["date"]] = df[["date"]].apply(pd.to_datetime)

		# print("columns grouped by data type: " + str(df.columns.to_series().groupby(df.dtypes).groups))

		print("	  connecting to MicroStrategy at: " + str(datetime.datetime.now()))

		from mstrio import microstrategy
		conn = microstrategy.Connection(base_url="https://env-124258.customer.cloud.microstrategy.com/MicroStrategyLibrary/api", username="jmaddocks", password="Qqd3BB66PJyt", project_name="Maddocks")
		conn.connect()

		df = pd.DataFrame(df, columns=df.columns.values)

		# use create_dataset to create a new cube
		# newDatasetId, newTableId = conn.create_dataset(data_frame=df, dataset_name='Chicago Beach Weather', table_name='ChicagoBeachWeather')

		# use update_dataset to update an existing cube
		# cubeID = existing cube ID (after running create_dataset above)
		conn.update_dataset(data_frame=df, dataset_id=strCubeID, table_name=strTableName, update_policy='add')

		conn.close()

		print("	  MicroStrategy update completed at: " + str(datetime.datetime.now()))

	else:

		print("    query returned no results")
