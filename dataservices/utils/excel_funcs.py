
def get_excel_file(sheet_name):
    from dataservices.utils.file_funcs import get_loc
    import pandas as pd
    return pd.read_excel(get_loc() + "data_services.xlsx", sheet_name=sheet_name)
