# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

####pandas####
#Series
obj = Series([4, 7, -5, 3])
obj

obj.values
obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2

obj2.index

obj2['a']

obj2['d'] = 6
obj2[['c', 'a', 'd']]

obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)

'b' in obj2
'e' in obj2

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4

pd.isnull(obj4)
pd.notnull(obj4)

obj4.isnull()

obj3
obj4
obj3 + obj4

obj4.name = 'population'
obj4.index.name = 'state'
obj4

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

#dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame

DataFrame(data, columns=['year', 'state', 'pop'])

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2.columns

frame2['state']
frame2.year
frame2.ix['three']

frame2['debt'] = 16.5
frame2

frame2['debt'] = np.arange(5.)
frame2

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2

frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2.columns

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
frame3

frame3.T

DataFrame(pop, index=[2001, 2002, 2003])

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
DataFrame(pdata)

frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3
frame3.values
frame2.values

#索引对象
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index

index[1:]

index[1] = 'd'

index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index

frame3
'Ohio' in frame3.columns
2003 in frame3.index

#基本功能
df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
df

df.sum()
df.apply(lambda x: x ** 2)
df ** 2

df.append({'numbers': 100, 'floats': 5.75, 'names': 'Henry'},
               ignore_index=True)
               
df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75,
                             'names': 'Henry'}, index=['z',]))
df

df.join(pd.DataFrame([1, 4, 9, 16, 25],
            index=['a', 'b', 'c', 'd', 'y'],
            columns=['squares',]))

df = df.join(pd.DataFrame([1, 4, 9, 16, 25],
                    index=['a', 'b', 'c', 'd', 'y'],
                    columns=['squares',]),
                    how='outer')
df

df[['numbers', 'squares']].mean()

df[['numbers', 'squares']].std()



###dataframe合并
#1
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
df1
df2

pd.merge(df1, df2)
pd.merge(df1, df2, on='key')

#2
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

pd.merge(df1, df2, how='outer')

#3
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
df1
df2

pd.merge(df1, df2, on='key', how='left')
pd.merge(df1, df2, how='inner')

#4
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
pd.merge(left, right, on=['key1', 'key2'], how='outer')

#5
pd.merge(left, right, on='key1')

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))


###索引上的合并
#1
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
left1
right1

pd.merge(left1, right1, left_on='key', right_index=True)

pd.merge(left1, right1, left_on='key', right_index=True, how='outer')

#2
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])
lefth
righth

pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)

pd.merge(lefth, righth, left_on=['key1', 'key2'],
         right_index=True, how='outer')

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                 columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
left2
right2
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)

#3
left2.join(right2, how='outer')

left1.join(right1, on='key')

#4
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
left2.join([right2, another])

left2.join([right2, another], how='outer')


###轴向连接
#1
arr = np.arange(12).reshape((3, 4))
arr

np.concatenate([arr, arr], axis=1)

#2
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])

pd.concat([s1, s2, s3], axis=1)

s4 = pd.concat([s1 * 5, s3])
pd.concat([s1, s4], axis=1)

pd.concat([s1, s4], axis=1, join='inner')

pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])

#3
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result

result.unstack()

#4
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])

pd.concat({'level1': df1, 'level2': df2}, axis=1)

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])

#5
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

df1

df2

pd.concat([df1, df2], ignore_index=True)


###合并重叠数据
#1
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan

a

b

np.where(pd.isnull(a), b, a)

#2
b[:-2].combine_first(a[2:])

#3
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
df1.combine_first(df2)


###重塑层次化索引
#1
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
data

result = data.stack()
result

result.unstack()

result.unstack(0)

result.unstack('state')

#2
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2.unstack()

data2.unstack().stack()

data2.unstack().stack(dropna=False)

#3
df = DataFrame({'left': result, 'right': result + 5},
               columns=pd.Index(['left', 'right'], name='side'))
df

df.unstack('state')

df.unstack('state').stack('side')


###长宽格式的转换
#1
data = pd.read_csv('d:/data/macrodata.csv')
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
data = DataFrame(data.to_records(),
                 columns=pd.Index(['realgdp', 'infl', 'unemp'], name='item'),
                 index=periods.to_timestamp('D', 'end'))

ldata = data.stack().reset_index().rename(columns={0: 'value'})
wdata = ldata.pivot('date', 'item', 'value')

#2
ldata[:10]

pivoted = ldata.pivot('date', 'item', 'value')
pivoted.head()

ldata['value2'] = np.random.randn(len(ldata))
ldata[:10]

pivoted = ldata.pivot('date', 'item')
pivoted[:5]

pivoted['value'][:5]

unstacked = ldata.set_index(['date', 'item']).unstack('item')
unstacked[:7]


###移除重复数据
data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
data

data.duplicated()

data.drop_duplicates()

data['v1'] = range(7)
data.drop_duplicates(['k1'])

data.drop_duplicates(['k1', 'k2'], take_last=True)


###利用函数或映射进行数据转换
#1
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data

data['food'].map(lambda x: meat_to_animal[x.lower()])



###替换值
data = Series([1., -999., 2., -999., -1000., 3.])
data

data.replace(-999, np.nan)

data.replace([-999, -1000], np.nan)

data.replace([-999, -1000], [np.nan, 0])

data.replace({-999: np.nan, -1000: 0})



###基本分析
df.describe()
np.sqrt(df)
np.sqrt(df).sum()

get_ipython().magic(u'matplotlib inline')
df.cumsum().plot(lw=2.0, grid=True)

dates = pd.date_range('2015-1-1', periods=9, freq='M')
dates
          
#GroupBy 技术
df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randn(5),
                'data2' : np.random.randn(5)})
df

grouped = df['data1'].groupby(df['key1'])
grouped

grouped.mean()


means = df['data1'].groupby([df['key1'], df['key2']]).mean()
means

means.unstack()

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()

df.groupby('key1').mean()

df.groupby(['key1', 'key2']).mean()

df.groupby(['key1', 'key2']).size()


# 对分组进行迭代
for name, group in df.groupby('key1'):
    print(name)
    print(group)

df.groupby('key1')

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)

pieces = dict(list(df.groupby('key1')))
pieces['b']

df.dtypes

grouped = df.groupby(df.dtypes, axis=1)
dict(list(grouped))


# 选择一个或一组列
df.groupby('key1')['data1']
df.groupby('key1')[['data2']]
df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1'])

df.groupby(['key1', 'key2'])[['data2']].mean()

s_grouped = df.groupby(['key1', 'key2'])['data2']
s_grouped

s_grouped.mean()


#  通过字典或series进行分组
people = DataFrame(np.random.randn(5, 5),
                   columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.ix[2:3, ['b', 'c']] = np.nan # Add a few NA values
people

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}

by_column = people.groupby(mapping, axis=1)
by_column.sum()

map_series = Series(mapping)
map_series

people.groupby(map_series, axis=1).count()


#通过函数进行分组
people.groupby(len).sum()

key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()


#  通过索引进行分组
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                    [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
hier_df = DataFrame(np.random.randn(4, 5), columns=columns)
hier_df

hier_df.groupby(level='cty', axis=1).count()

####Python时间序列的处理
from datetime import datetime
now = datetime.now()
now

now.year, now.month, now.day

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta

delta.days

delta.seconds


from datetime import timedelta
start = datetime(2011, 1, 7)
start + timedelta(12)

start - 2 * timedelta(12)


#字符串转日期
stamp = datetime(2011, 1, 3)
str(stamp)
stamp.strftime('%Y-%m-%d')

value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')

datestrs = ['7/6/2011', '8/6/2011']
[datetime.strptime(x, '%m/%d/%Y') for x in datestrs]

from dateutil.parser import parse
parse('2011-01-03')
parse('Jan 31, 1997 10:45 PM')
parse('6/12/2011', dayfirst=True)

datestrs
pd.to_datetime(datestrs)

idx = pd.to_datetime(datestrs + [None])
idx
idx[2]
pd.isnull(idx)


#pands中的时间序列
from datetime import datetime
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = Series(np.random.randn(6), index=dates)
ts
type(ts)

ts.index

ts + ts[::2]

ts.index.dtype

stamp = ts.index[0]
stamp


#索引、选取与子集构造
stamp = ts.index[2]
ts[stamp]

ts['1/10/2011']

ts['20110110']

longer_ts = Series(np.random.randn(1000),
                   index=pd.date_range('1/1/2000', periods=1000))
longer_ts

longer_ts['2001']

longer_ts['2001-05']

ts[datetime(2011, 1, 7):]
ts

ts['1/6/2011':'1/11/2011']

ts.truncate(after='1/9/2011')

dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = DataFrame(np.random.randn(100, 4),
                    index=dates,
                    columns=['Colorado', 'Texas', 'New York', 'Ohio'])
long_df.ix['5-2001']

#
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000',
                          '1/3/2000'])
dup_ts = Series(np.arange(5), index=dates)
dup_ts

dup_ts.index.is_unique

dup_ts['1/3/2000'] 

dup_ts['1/2/2000']

grouped = dup_ts.groupby(level=0)
grouped.mean()

grouped.count()


#日期范围、频率与移动
ts
ts.resample('D').mean()

index = pd.date_range('4/1/2012', '6/1/2012')
index

pd.date_range(start='4/1/2012', periods=20)

pd.date_range(end='6/1/2012', periods=20)

pd.date_range('1/1/2000', '12/1/2000', freq='BM')

pd.date_range('5/2/2012 12:56:31', periods=5)

pd.date_range('5/2/2012 12:56:31', periods=5, normalize=True)

from pandas.tseries.offsets import Hour, Minute
hour = Hour()
hour


four_hours = Hour(4)
four_hours

pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')

Hour(2) + Minute(30)

pd.date_range('1/1/2000', periods=10, freq='1h30min')


rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')
list(rng)


ts = Series(np.random.randn(4),
            index=pd.date_range('1/1/2000', periods=4, freq='M'))
ts

ts.shift(2)

ts.shift(-2)

ts / ts.shift(1) - 1

ts.shift(2, freq='M')

ts.shift(3, freq='D')

ts.shift(1, freq='3D')

ts.shift(1, freq='90T')


from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
now + 3 * Day()

now + MonthEnd()

now + MonthEnd(2)

offset = MonthEnd()
offset.rollforward(now)

offset.rollback(now)



ts = Series(np.random.randn(20),
            index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean()

ts.resample('M').mean()


##时间序列可视化
import matplotlib.pyplot as plt
close_px_all = pd.read_csv('d:/data/stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
close_px.info()

close_px['AAPL'].plot()

close_px.ix['2009'].plot()

close_px['AAPL'].ix['01-2011':'03-2011'].plot()

appl_q = close_px['AAPL'].resample('Q-DEC').ffill()
appl_q.ix['2009':].plot()

close_px = close_px.asfreq('B').fillna(method='ffill').ffill()

close_px.AAPL.plot()
pd.rolling_mean(close_px.AAPL, 250).plot()

plt.figure()

appl_std250 = pd.rolling_std(close_px.AAPL, 250, min_periods=10)
appl_std250[5:12]

appl_std250.plot()

expanding_mean = lambda x: rolling_mean(x, len(x), min_periods=1)

pd.rolling_mean(close_px, 60).plot(logy=True)

plt.close('all')

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True,
                         figsize=(12, 7))

aapl_px = close_px.AAPL['2005':'2009']

ma60 = pd.rolling_mean(aapl_px, 60, min_periods=50)
ewma60 = pd.ewma(aapl_px, span=60)

aapl_px.plot(style='k-', ax=axes[0])
ma60.plot(style='k--', ax=axes[0])
aapl_px.plot(style='k-', ax=axes[1])
ewma60.plot(style='k--', ax=axes[1])
axes[0].set_title('Simple MA')
axes[1].set_title('Exponentially-weighted MA')

close_px
spx_px = close_px_all['SPX']


spx_rets = spx_px / spx_px.shift(1) - 1
returns = close_px.pct_change()
corr = pd.rolling_corr(returns.AAPL, spx_rets, 125, min_periods=100)
corr.plot()

corr = pd.rolling_corr(returns, spx_rets, 125, min_periods=100)
corr.plot()


from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = pd.rolling_apply(returns.AAPL, 250, score_at_2percent)
result.plot()

####金融数据####
#DataReader
import pandas.io.data as web
DAX = web.DataReader(name='^GDAXI', data_source='yahoo',
                     start='2000-1-1')
DAX.info()
DAX.tail()
DAX['Close'].plot(figsize=(8, 5), grid=True)

#对数收益率计算

#DAX['Ret_Loop'] = 0.0
#for i in range(1, len(DAX)):
#    DAX['Ret_Loop'][i] = np.log(DAX['Close'][i] /
#                                DAX['Close'][i - 1])
#DAX[['Close', 'Ret_Loop']].tail()
                                
get_ipython().magic(u"time DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))")

DAX[['Close', 'Return']].tail()


DAX[['Close', 'Return']].plot(subplots=True, style='b',
                              figsize=(8, 5), grid=True)
                              
#移动平均
DAX['42d'] = pd.rolling_mean(DAX['Close'], window=42)
DAX['252d'] = pd.rolling_mean(DAX['Close'], window=252)
DAX[['Close', '42d', '252d']].tail()

DAX[['Close', '42d', '252d']].plot(figsize=(8, 5), grid=True)

#历史波动率
import math
DAX['Mov_Vol'] = pd.rolling_std(DAX['Return'],
                                window=252) * math.sqrt(252)
DAX[['Close','Mov_Vol','Return']].plot(subplots=True,style='b',figsize=(8,7))
                                
####高频数据####
import numpy as np
import pandas as pd
import datetime as dt
from urllib import urlretrieve
get_ipython().magic(u'matplotlib inline')

url1 = 'http://www.netfonds.no/quotes/posdump.php?'
url2 = 'date=%s%s%s&paper=NKE.N&csv_format=csv' 
url = url1 + url2

year = '2016'
month = '08'
days = [ '22', '23', '24','25','26']

NKE = pd.DataFrame()
for day in days:
    NKE = NKE.append(pd.read_csv(url % (year, month, day),
                       index_col=0, header=0, parse_dates=True))
NKE.columns = ['bid', 'bdepth', 'bdeptht', 'offer', 'odepth', 'odeptht']

NKE.info()

NKE['bid'].plot(grid=True)

to_plot = NKE[['bid', 'bdeptht']][
    (NKE.index > dt.datetime(2016, 8, 24, 0, 0))
 &  (NKE.index < dt.datetime(2016, 8, 25, 2, 59))]
  # adjust dates to given data set
to_plot.plot(subplots=True, style='b', figsize=(8, 5), grid=True)

NKE_resam = NKE.resample(rule='5min').mean()
np.round(NKE_resam.head(), 2)

NKE_resam['bid'].fillna(method='ffill').plot(grid=True)

def reversal(x):
    return 2 * 95 - x

NKE_resam['bid'].fillna(method='ffill').apply(reversal).plot(grid=True)

                            