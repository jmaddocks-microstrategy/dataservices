from dataservices.utils.excel_funcs import get_excel_file
from dataservices.utils.query_data_services import create_cube

# change str_where_clause and str_slice_name to match the dataservice and slice you're updating
str_where_clause = " between '2018-07-17T00:00:00.000' and '2019-03-02T23:59:59.000'"
str_slice_name = 'ChicagoCrime'

df = get_excel_file()   # used for reading

# take this slice of the dataframe
df = df[df['Name'] == str_slice_name]

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

# update the cube
new_dataset_id = create_cube("update", str_table_name, str_url, str_app_token, str_user_name, str_password, str_webservice_id, str_date_field, i_months_of_data, str_cube_id=str_cube_id, str_where_clause=str_where_clause)
