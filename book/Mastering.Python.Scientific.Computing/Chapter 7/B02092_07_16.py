import numpy as np
randn = np.random.randn
from pandas import *
from pandas.tseries.offsets import *

start = datetime(2005, 1, 1)
end = datetime(2015, 1, 1)
rng = date_range(start, end, freq='BM')
ts = Series(randn(len(rng)), index=rng)
ts.index
ts[:8].index
ts[::1].index

# We can directly use the dates and Strings for index 
ts['8/31/2012']
ts[datetime(2012, 07, 11):]
ts['10/08/2005':'12/31/2014']
ts['2012']
ts['2012-7']

dft = DataFrame(randn(50000,1),columns=['X'],index=date_range('20050101',periods=50000,freq='T'))
dft
dft['2005']
# first time of the first month and last time of month in parameter after :
dft['2005-1':'2013-4']
dft['2005-1':'2005-3-31']
# We can specify stop time
dft['2005-1':'2005-3-31 00:00:00']
dft['2005-1-17':'2005-1-17 05:30:00']
#Datetime indexing
dft[datetime(2005, 1, 1):datetime(2005,3,31)]
dft[datetime(2005, 1, 1, 01, 02, 0):datetime(2005, 3, 31, 01, 02, 0)]

#selection of single row using loc
dft.loc['2005-1-17 05:30:00']

# time trucation
ts.truncate(before='1/1/2010', after='12/31/2012')
