
def get_excel_file():
    from dataservices.utils.file_funcs import get_loc
    import pandas as pd

    return pd.read_excel(get_loc() + "data_services.xlsx", sheet_name="data_services")


def write_excel_file(df):
    import pandas as pd
    from dataservices.utils.file_funcs import get_loc

    writer = pd.ExcelWriter(get_loc() + "data_services.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="data_services")
    writer.save()
