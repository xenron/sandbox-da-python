import pandas as pd
import numpy as np

Y2K = pd.date_range('2000-01-01', '2000-12-31')
print Y2K

Y2K_hourly = pd.date_range('2000-01-01', '2000-12-31', freq='H')
Y2K_temp = pd.Series(np.random.normal(75, 10, len(Y2K)), index=Y2K)

Y2K_temp['2000-01-01':'2000-01-02']
from datetime import date
Y2K_temp[date(2000, 1, 1):date(2000, 1, 2)]
Y2K_temp.resample('H', fill_method='pad')[:1]
print Y2K_temp
