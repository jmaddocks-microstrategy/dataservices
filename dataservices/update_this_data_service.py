from dataservices.utils.excel_funcs import get_excel_file
from dataservices.utils.query_data_services import run_query

# change str_where_clause and str_slice_name to match the dataservice and slice you're updating
str_where_clause = "between '2019-01-01T00:00:00.000' and '2019-03-01T23:59:59.000'"
str_slice_name = 'ChicagoCrime'

df = get_excel_file()   # used for reading

# take this slice of the dataframe
df_slice = df[df['Name'] == str_slice_name]
df_slice = df_slice.iloc[0]

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

# finalize the where clause by piping in the name of the date field
str_where_clause = str_date_field + " " + str_where_clause

# update the cube
new_dataset_id = run_query("update", str_table_name, str_url, str_app_token, str_user_name, str_password, str_webservice_id, str_cube_id, str_where_clause)
