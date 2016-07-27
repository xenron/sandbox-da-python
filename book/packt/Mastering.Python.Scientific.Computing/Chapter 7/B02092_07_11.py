import numpy as np
randn = np.random.randn
from pandas import *

index = date_range('1/1/2000', periods=10)

s = Series(randn(10), index=[’I’, ’II’, ’III’, ’IV’, ’V’, ’VI’, ’VII’, ’VIII’, ’IX’, ’X’ ])

df = DataFrame(randn(10, 4), index=[’I’, ’II’, ’III’, ’IV’, ’V’, ’VI’, ’VII’, ’VIII’, ’IX’, ’X’ ], columns=['A', 'B', 'C', 'D']) 

workpanel = Panel(randn(2, 3, 5), items=[’FirstItem’, ’SecondItem’],
     major_axis=date_range(’1/1/2010’, periods=3),
     minor_axis=[’A’, ’B’, ’C’, ’D’, ’E’])

series_with100elements = Series(randn(100))

series_with100elements.head()
series_with100elements.tail(3)

series_with100elements[:2]
df[:2]
workpanel[:2]

df.columns = [x.lower() for x in df.columns]
df

# Values property can be used to access the actual value.
s.values
df.values
wp.values

series = Series(randn(440))
series[20:440] = np.nan
series[10:20]  = 5
series.nunique()
series = Series(randn(1700))
series[::3] = np.nan
series.describe()

frame = DataFrame(randn(1200, 5), columns=['a', 'e', 'i', 'o', 'u'])
frame.ix[::3] = np.nan
frame.describe()

series.describe(percentiles=[.05, .25, .75, .95])
s = Series(['x', 'x', 'y', 'y', 'x', 'x', np.nan, 'u', 'v', 'x'])
s.describe()

frame = DataFrame({'x': ['Y', 'Yes', 'Yes', 'N', 'No', 'No'], 'y': range(6)})
frame.describe()
frame.describe(include=['object'])
frame.describe(include=['number'])
frame.describe(include='all')