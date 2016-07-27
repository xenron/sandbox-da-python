import numpy as np
randn = np.random.randn
from pandas import *

# Date Range creation, 152 hours from 06/03/2015
range_date = date_range('6/3/2015', periods=152, freq='H')
range_date[:5]

# Indexing on the basis of date
ts = Series(randn(len(rng)), index=rng)
ts.head()

#change the frequency to 40 Minuntes
converted = ts.asfreq('40Min', method='pad')
converted.head()
ts.resample('D', how='mean')
dates = [datetime(2015, 6, 10), datetime(2015, 6, 11), datetime(2015, 6, 12)]
ts = Series(np.random.randn(3), dates)
type(ts.index)
ts

#creation of period index
periods = PeriodIndex([Period('2015-10'), Period('2015-11'),
                       Period('2015-12')])
ts = Series(np.random.randn(3), periods)
type(ts.index)
ts

# Convertion to Timestamp
to_datetime(Series(['Jul 31, 2014', '2015-01-08', None]))
to_datetime(['1995/10/31', '2005.11.30'])
# dayfirst to represent the data starts with day
to_datetime(['01-01-2015 11:30'], dayfirst=True)
to_datetime(['14-03-2007', '03-14-2007'], dayfirst=True)
# Invalid data can be converted to NaT using coerce=True
to_datetime(['2012-07-11', 'xyz'])
to_datetime(['2012-07-11', 'xyz'], coerce=True)

#doesn't works properly on mixed datatypes
to_datetime([1, '1'])
# Epoch timestamp : Integer and float epoch times can be converted to timestamp
# the default using is nenoseconds that can be changed to seconds/ microseconds
# The base time is 01/01/1970
to_datetime([1449720105, 1449806505, 1449892905,
             1449979305, 1450065705], unit='s')
to_datetime([1349720105100, 1349720105200, 1349720105300,
             1349720105400, 1349720105500 ], unit='ms')
to_datetime([8])
to_datetime([8, 4.41], unit='s')

#Datetime Range 
dates = [datetime(2015, 4, 10), datetime(2015, 4, 11), datetime(2015, 4, 12)]
index = DatetimeIndex(dates)
index = Index(dates)
index = date_range('2010-1-1', periods=1700, freq='M')
index
index = bdate_range('2014-10-1', periods=250)
index

start = datetime(2005, 1, 1)
end = datetime(2015, 1, 1)
range1 = date_range(start, end)
range1
range2 = bdate_range(start, end)
range2