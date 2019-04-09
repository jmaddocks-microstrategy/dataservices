import schedule
import time
from dataservices.utils.file_funcs import initialize_log_file
from dataservices.utils.other_funcs import check_time_interval
from dataservices.utils.config_funcs import read_config_value

i_check_interval_seconds = int(read_config_value('SETTINGS', 'checkintervalseconds'))

initialize_log_file()

print("DataServices scheduler has started.")

schedule.every(i_check_interval_seconds).seconds.do(check_time_interval)

while True:
    schedule.run_pending()
    time.sleep(1)
