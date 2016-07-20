import numpy as np
randn = np.random.randn
from pandas import *

df = DataFrame({'one-1' : Series(randn(3), index=['a', 'b', 'c']),
                'two-2' : Series(randn(4), index=['a', 'b', 'c', 'd']),
				'three-3' : Series(randn(3), index=['b', 'c', 'd'])})
df
df.mean(0)
df.mean(1)
df.mean(0, skipna=False)
df.mean(axis=1, skipna=True)
df.sum(0)
df.sum(axis=1)
df.sum(0, skipna=False)
df.sum(axis=1, skipna=True)

# the NumPy methods excludes missing values
np.mean(df['one-1'])
np.mean(df['one-1'].values)

ser = Series(randn(10))
ser.pct_change(periods=3)

# Percentage change over a given period 
df = DataFrame(randn(8, 4))
df.pct_change(periods=2)

ser1 = Series(randn(530))
ser2 = Series(randn(530))
ser1.cov(ser2)

frame = DataFrame(randn(530, 5), columns=['i', 'ii', 'iii', 'iv', 'v'])
frame.cov()
frame = DataFrame(randn(26, 3), columns=['x', 'y', 'z'])
frame.ix[:8, 'i'] = np.nan
frame.ix[8:12, 'ii'] = np.nan
frame.cov()
frame.cov(min_periods=10)
frame = DataFrame(randn(530, 5), columns=['i', 'ii', 'iii', 'iv', 'v'])
frame.ix[::4] = np.nan

# By pearson (Default) method Standard correlation coefficient
frame['i'].corr(frame['ii'])
# We can specify method Kendall/ spearman
frame['i'].corr(frame['ii'], method='kendall')
frame['i'].corr(frame['ii'], method='spearman')

index = ['i', 'ii', 'iii', 'iv']
columns = ['first', 'second', 'third']
df1 = DataFrame(randn(4, 3), index=index, columns=columns)
df2 = DataFrame(randn(3, 3), index=index[:3], columns=columns)
df1.corrwith(df2)
df2.corrwith(df1, 1)

s = Series(np.random.randn(10), index=list('abcdefghij'))
s['d'] = s['b'] # so there's a tie
s.rank()

df = DataFrame(np.random.randn(8, 5))
df[4] = df[2][:5] # some ties
df
df.rank(1)