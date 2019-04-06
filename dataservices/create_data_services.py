
import os
import sys
import pathlib
import pandas as pd
from dataservices.utils.query_data_services import create_cube

loc = os.fspath(pathlib.Path(pathlib.Path(sys.path[0]))) + "/"

df = pd.read_excel(loc + "data_services.xlsx", sheet_name="create")

for i in range(0, len(df)):
    ar_this_service = df.iloc[i]

    str_table_name = ar_this_service[0]
    str_url = ar_this_service[1]
    str_app_token = ar_this_service[2]
    str_user_name = ar_this_service[3]
    str_password = ar_this_service[4]
    str_webservice_id = ar_this_service[5]
    str_date_field = ar_this_service[6]
    i_months_of_data = int(ar_this_service[7])

    create_cube(loc, str_table_name, str_url, str_app_token, str_user_name, str_password, str_webservice_id, str_date_field, i_months_of_data)


def write_cube_id():
    from dataservices.utils.excel_functions import

    loc = os.fspath(pathlib.Path(pathlib.Path(sys.path[0]))) + "/"

    df = pd.read_excel(loc + "data_services.xlsx", sheet_name="create")