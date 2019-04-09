
def check_time_interval():
    import datetime
    from dataservices.utils.file_funcs import get_log_file
    from dataservices.utils.time_intervals import calculate_time_since_last_run
    from dataservices.utils.config_funcs import read_config_value

    if calculate_time_since_last_run() >= int(read_config_value('SETTINGS', 'queryintervalminutes')):
        print("  will query webservices now")

        log_file = get_log_file("w")
        log_file.seek(0)
        log_file.write("queried data at: " + str(datetime.datetime.now()))
        log_file.close()
        query_from_configuration("scheduled")
        return 1

    else:
        print("  will not query webservices at this time")
        return 0


def query_from_configuration(str_query_type):
    from dataservices.utils.excel_funcs import get_excel_file
    from dataservices.utils.excel_funcs import write_excel_file
    from dataservices.utils.query_data_services import run_query
    from dataservices.utils.time_intervals import get_start_date

    df = get_excel_file()  # used for reading

    if str_query_type == "create":
        df2 = df.copy()  # used for writing

    # loop thru leach row in the excel file
    for i in range(0, len(df)):
        # take this slice of the dataframe
        df_slice = df.iloc[i]

        # get the webservices properties for this slice
        str_table_name = df_slice['Name']
        str_url = df_slice['dsURL']
        str_app_token = df_slice['dsApptoken']
        str_user_name = df_slice['dsUserName']
        str_password = df_slice['dsPassword']
        str_webservice_id = df_slice['dsWebserviceID']
        str_date_field = df_slice['dsDateField']
        i_months_of_data = int(df_slice['dsMonthsOfData'])
        str_cube_id = df_slice['mstrCubeID']

        # handle building the where clause based on date in the excel file
        dt_start_date = get_start_date(i_months_of_data)
        str_where_clause = str_date_field + " > '" + str(dt_start_date) + "T00:00:00.000'"

        # create the cube
        new_dataset_id = run_query(str_query_type, str_table_name, str_url, str_app_token, str_user_name, str_password,
                                   str_webservice_id, str_cube_id, str_where_clause)

        if str_query_type == "create":  # now that the cube is created, write the cube ID back to the excel file
            if len(new_dataset_id) > 0:
                df2.loc[df2['Name'] == str_table_name, 'mstrCubeID'] = new_dataset_id
                write_excel_file(df2)
