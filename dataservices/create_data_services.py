
def write_cube_id(df_slice, new_dataset_id):
    df_slice[8] = new_dataset_id




from dataservices.utils.excel_funcs import get_excel_file
from dataservices.utils.query_data_services import create_cube

df = get_excel_file("data_services")

for i in range(0, len(df)):

    df_slice = df.iloc[i]
    str_table_name = df_slice[0]
    str_url = df_slice[1]
    str_app_token = df_slice[2]
    str_user_name = df_slice[3]
    str_password = df_slice[4]
    str_webservice_id = df_slice[5]
    str_date_field = df_slice[6]
    i_months_of_data = int(df_slice[7])

    new_dataset_id = create_cube(str_table_name, str_url, str_app_token, str_user_name, str_password, str_webservice_id, str_date_field, i_months_of_data)
    # if len(new_dataset_id) > 0:  write_cube_id(df_slice, new_dataset_id)
    if len(new_dataset_id) > 0: df_slice[8] = new_dataset_id

