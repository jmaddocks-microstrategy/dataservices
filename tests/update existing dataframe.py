import pandas as pd
import numpy as np

# https://pythonfordatascience.org/merge-and-update-pandas-data-frame/

org_df = pd.DataFrame({'ID': ['11', '12', '13', '14'],
                       'NAME': ['Kiara', 'Rajah', 'Simba', np.nan],
                       'TEST 1': [66, 99, 75, 23]})

new_data_df = pd.DataFrame({'ID': ['11', '14', '15'],
                       'NAME': ['Kiara', 'Wilbert', 'Momma'],
                       'TEST 1': [75, np.nan, 23]})

print()