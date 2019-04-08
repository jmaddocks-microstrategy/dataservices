
def getServices(loc):

    import pandas as pd

    df = pd.read_excel(loc+"data_services.xlsx", sheet_name="Sheet1")

    for i in range(0, len(df)):
        ar_this_service = df.iloc[i]
        update_cubes(ar_this_service)


def update_cubes(arThisService):

    str_table_name = arThisService[0]
    str_url = arThisService[1]
    str_app_token = arThisService[2]
    str_user_name = arThisService[3]
    str_password = arThisService[4]
    str_webservice_id = arThisService[5]
    str_date_field = arThisService[6]
    i_months_of_data = int(arThisService[7])
    str_cube_id = arThisService[8]

    import pandas as pd
    from sodapy import Socrata
    import datetime
    from datetime import date
    from dateutil.relativedelta import relativedelta

    dt_start_date = date.today() + relativedelta(months=-1*i_months_of_data)

    client = Socrata(str_url,
                     str_app_token,
                     username=str_user_name,
                     password=str_password
                     )

    print("	" + str_table_name + " query started at: " + str(datetime.datetime.now()))

    strDataQuery = str_date_field + " > '" + str(dt_start_date) + "T00:00:00.000'"
    #strDataQuery = str_date_field + " between '2018-07-17T00:00:00.000' and '2019-03-02T23:59:59.000'"

    print("	  using query: '" + strDataQuery + "'")
    results = client.get(str_webservice_id, where=strDataQuery, limit=99999999)
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
        conn.update_dataset(data_frame=df, dataset_id=str_cube_id, table_name=str_table_name, update_policy='add')

        conn.close()

        print("	  MicroStrategy update completed at: " + str(datetime.datetime.now()))

    else:

        print("    query returned no results")


def run_query(str_query_type, str_table_name, str_url, str_app_token, str_user_name, str_password, str_webservice_id, str_cube_id, str_where_clause):

    import pandas as pd
    import datetime
    from sodapy import Socrata
    from dataservices.utils.config_funcs import read_config_value

    client = Socrata(str_url,
                    str_app_token,
                    username=str_user_name,
                    password=str_password
                    )

    print("	" + str_table_name + " query started at: " + str(datetime.datetime.now()))

    print("	  using query: '" + str_where_clause + "'")

    # query the webservice using the appropriate where clause
    results = client.get(str_webservice_id, where=str_where_clause, limit=99999999)
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
        conn = microstrategy.Connection(base_url=read_config_value('MSTR_LIBRARY', 'rest_api_url'), username=read_config_value('MSTR_LIBRARY', 'username'), password=read_config_value('MSTR_LIBRARY', 'password'), project_name=read_config_value('MSTR_LIBRARY', 'project'))
        conn.connect()

        df = pd.DataFrame(df, columns=df.columns.values)

        # query mstrio differently depending on the type of update
        if str_query_type == "create":  # creates should use the create_dataset method

            new_dataset_id, newTableId = conn.create_dataset(data_frame=df, dataset_name=str_table_name,
                                                             table_name=str_table_name)

        elif str_query_type == "update" or _str_query_type == "scheduled":  # updates or scheduled should use the update method

            conn.update_dataset(data_frame=df, dataset_id=str_cube_id, table_name=str_table_name, update_policy='add')
            new_dataset_id = str_cube_id

        else:

            conn.close()
            print("	mstrio not updated, was this in error??")
            return ""

        conn.close()
        print("	  MicroStrategy update completed at: " + str(datetime.datetime.now()))
        return str(new_dataset_id)

    else:

        print("    query returned no results")
        return ""
