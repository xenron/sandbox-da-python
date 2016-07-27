import numpy as np
randn = np.random.randn
from pandas import *

df = DataFrame(randn(8, 4), index=[’I’, ’II’, ’III’, ’IV’, ’VI’, ’VII’, ’VIII’, ’X’ ], 
		columns=['A', 'B', 'C', 'D']) 

df[’E’] = ’Dummy’
df[’F’] = df[’A’] > 0.5
df

# Introducing some Missing data by adding new index
df2 = df.reindex([’I’, ’II’, ’III’, ’IV’, ’V’, ’VI’, ’VII’, ’VIII’, ’IX’, ’X’])
df2
df2[’A’]
#Checking for missing values
isnull(df2[’A’])
df2[’D’].notnull()

df3 = df.copy()
df3[’timestamp’] = Timestamp(’20120711’)
df3
# Observe the output of timestamp column for missing values as NaT
df3.ix[[’I’,’III’,’VIII’],[’A’,’timestamp’]] = np.nan
df3

s = Series([5,6,7,8,9])
s.loc[0] = None
s

s = Series(["A", "B", "C", "D", "E"])
s.loc[0] = None
s.loc[1] = np.nan
s

# Fillna method to fill the missing value
df2
df2.fillna(0)  # fill all missing value with 0
df2[’D’].fillna(’missing’) # fill particular column missing value with missing

df2.fillna(method=’pad’)
df2
df2.fillna(method=’pad’, limit=1)

df2.dropna(axis=0)
df2.dropna(axis=1)

ts
ts.count()
ts[10:30]=None
ts.count()
# interpolate method perform interpolation to fill the missing values
# By degfault it performs linear interpolation 
ts.interpolate()
ts.interpolate().count()