import numpy as np
randn = np.random.randn
from pandas import *

workpanel = Panel(randn(2, 3, 5), items=[’FirstItem’, ’SecondItem’],
     major_axis=date_range(’1/1/2010’, periods=3),
     minor_axis=[’A’, ’B’, ’C’, ’D’, ’E’])
df = DataFrame({'one-1' : Series(randn(3), index=['a', 'b', 'c']),
                'two-2' : Series(randn(4), index=['a', 'b', 'c', 'd']),
				'three-3' : Series(randn(3), index=['b', 'c', 'd'])})

for columns in df:
     print(columns)
 

for items, frames in workpanel.iteritems():
     print(items)
     print(frames)

for r_index, rows in df2.iterrows():
	     print('%s\n%s' % (r_index, rows))

df2 = DataFrame({'x': [1, 2, 3, 4, 5], 'y': [6, 7, 8, 9, 10]})
print(df2)
print(df2.T)

df2_t = DataFrame(dict((index,vals) for index, vals in df2.iterrows()))
print(df2_t)

df_iter = DataFrame([[1, 2.0, 3]], columns=['x', 'y', 'z'])
row = next(df_iter.iterrows())[1]

print(row['x'].dtype)
print(df_iter['x'].dtype)

for row in df2.itertuples():
    print(row)

# datetime handling using dt accessor 
s = Series(date_range('20150509 01:02:03',periods=5))
s
s.dt.hour
s.dt.second
s.dt.day
s[s.dt.day==2]

# Timezone based translation can be performed very easily
stimezone = s.dt.tz_localize('US/Eastern')
stimezone
stimezone.dt.tz
s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')

# period
s = Series(period_range('20150509',periods=5,freq='D'))
s
s.dt.year
s.dt.day

# timedelta
s = Series(timedelta_range('1 day 00:00:05',periods=4,freq='s'))
s
s.dt.days
s.dt.seconds
s.dt.components
