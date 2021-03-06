
def get_start_date(i_months_of_data):
    from datetime import date
    from dateutil.relativedelta import relativedelta
    return date.today() + relativedelta(months=-1 * i_months_of_data)


def calculate_time_since_last_run():
    import datetime
    from dateutil.relativedelta import relativedelta
    from dataservices.utils.file_funcs import get_log_file

    log_file = get_log_file("r")

    # figure out how long it's been since the last query
    ar_log = log_file.read().split(" ")
    str_last_ran = ar_log[3] + " " + ar_log[4]
    dt_now = datetime.datetime.now()
    dt_last_ran = datetime.datetime.strptime(str_last_ran, "%Y-%m-%d %H:%M:%S.%f")
    dt_difference = relativedelta(dt_now, dt_last_ran)
    i_minutes = dt_difference.minutes
    i_hours = dt_difference.hours
    i_days = dt_difference.days
    i_months = dt_difference.months
    i_years = dt_difference.years
    i_tot_min = (i_years*525600)+(i_months*43800)+(i_days*1440)+(i_hours*60)+i_minutes

    print(str(dt_now) + ": checking last query time ...")
    print("  ... " + str(i_tot_min) + " minutes since last webservices query (" + str(dt_last_ran) + ")")

    log_file.close()

    return i_tot_min
