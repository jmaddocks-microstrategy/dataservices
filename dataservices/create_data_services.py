from dataservices.utils.excel_funcs import get_excel_file
from dataservices.utils.excel_funcs import write_excel_file
from dataservices.utils.query_data_services import create_cube

df = get_excel_file()   # used for reading
df2 = df.copy()   # used for writing

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
    str_cube_id = df_slice['dsCubeID']

    # create the cube
    new_dataset_id = create_cube("create", str_table_name, str_url, str_app_token, str_user_name, str_password, str_webservice_id, str_date_field, i_months_of_data, str_cube_id)

    # now that the cube is created, write the cube ID back to the excel file
    if len(new_dataset_id) > 0:
        df2.loc[df2['Name'] == str_table_name, 'mstrCubeID'] = new_dataset_id
        write_excel_file(df2)
