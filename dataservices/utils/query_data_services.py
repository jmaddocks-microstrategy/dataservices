
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

        elif str_query_type == "update" or str_query_type == "scheduled":  # updates or scheduled should use the update method

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
