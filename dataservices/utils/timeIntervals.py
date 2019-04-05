
def calculate_time(s_log_file):

    import datetime
    from dateutil.relativedelta import relativedelta

    f = open(s_log_file, "r+")
    str_log = f.read()

    # figure out how long it's been since the last query
    ar_log = str_log.split(" ")
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

    f.close()

    return i_tot_min


def check_time_interval(loc, s_log_file, i_minutes_between_queries):

    import datetime
    from dataservices.utils.queryDataServices import getServices

    f = open(s_log_file, "r+")

    if calculate_time(s_log_file) >= i_minutes_between_queries:
        print("  will query webservices now")
        f.seek(0)
        f.write("queried data at: " + str(datetime.datetime.now()))
        f.truncate()
        getServices(str(loc))

    else:
        print("  will not query webservices at this time")
    f.close()
