
def update_cube(arThisService):

    str_table_name = arThisService[0]
    str_url = arThisService[1]
    str_app_token = arThisService[2]
    str_user_name = arThisService[3]
    str_password = arThisService[4]
    str_webservice_id = arThisService[5]
    str_date_field = arThisService[6]
    i_months_of_data = int(arThisService[7])

    import configparser
    import pandas as pd
    import datetime
    from datetime import date
    from dateutil.relativedelta import relativedelta
    from sodapy import Socrata

    dtStartDate = date.today() + relativedelta(months=-1*i_months_of_data)

    client = Socrata(str_url,
                    str_app_token,
                    username=str_user_name,
                    password=str_password
                    )

    print("	" + str_table_name + " query started at: " + str(datetime.datetime.now()))

    strDataQuery = str_date_field + " > '" + str(dtStartDate) + "T00:00:00.000'"
    #strDataQuery = strDateField + " between '2018-07-17T00:00:00.000' and '2019-03-02T23:59:59.000'"

    print("	  using query: '" + strDataQuery + "'")
    results = client.get(str_webservice_id, where=strDataQuery, limit=99999999)
    client.close()

    # Convert results to pandas DataFrame
    df = pd.DataFrame.from_records(results)
    if len(df.index) > 0:

        config = configparser.ConfigParser()
        config.read(loc + "dataservices.cfg")

        # convert series to the correct types
        # right now mstrio does not import datetime values ... so use this formula in Mstr to create a new datetime attribute: ToDateTime(LeftStr(date@ID, 10))
        # df[["date"]] = df[["date"]].apply(pd.to_datetime)

        # print("columns grouped by data type: " + str(df.columns.to_series().groupby(df.dtypes).groups))

        print("	  connecting to MicroStrategy at: " + str(datetime.datetime.now()))

        from mstrio import microstrategy
        conn = microstrategy.Connection(base_url=config['MSTR_LIBRARY']['rest_api_url'], username=config['MSTR_LIBRARY']['username'], password=config['MSTR_LIBRARY']['password'], project_name=config['MSTR_LIBRARY']['project'])
        conn.connect()

        df = pd.DataFrame(df, columns=df.columns.values)

        # use create_dataset to create a new cube
        newDatasetId, newTableId = conn.create_dataset(data_frame=df, dataset_name=str_table_name, table_name=str_table_name)

        # use update_dataset to update an existing cube
        # cubeID = existing cube ID (after running create_dataset above)
        #conn.update_dataset(data_frame=df, dataset_id=strCubeID, table_name=strTableName, update_policy='add')

        conn.close()

        print("	  MicroStrategy update completed at: " + str(datetime.datetime.now()))

    else:

        print("    query returned no results")


import os
import sys
import pathlib
import pandas as pd

loc = os.fspath(pathlib.Path(pathlib.Path(sys.path[0]))) + "/"

df = pd.read_excel(loc + "create_data_services.xlsx", sheet_name="Sheet1")

for i in range(0, len(df)):
    ar_this_service = df.iloc[i]
    update_cube(ar_this_service)
