# -*- coding: utf-8 -*-
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np
pd.options.display.max_rows = 12
np.set_printoptions(precision=4, suppress=True)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12, 4))



#
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

ts.resample('M', how='mean')


##时间序列可视化
close_px_all = pd.read_csv('d:/data/stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B', fill_method='ffill').ffill()
close_px.info()

close_px['AAPL'].plot()

close_px.ix['2009'].plot()

close_px['AAPL'].ix['01-2011':'03-2011'].plot()

appl_q = close_px['AAPL'].resample('Q-DEC', fill_method='ffill').ffill()
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

####时序案例分析####
#参数初始化
discfile = 'd:/data/arima_data.xls'
forecastnum = 5

#读取数据，指定日期列为指标，Pandas自动将“日期”列识别为Datetime格式
data = pd.read_excel(discfile, index_col = u'日期')
data = pd.DataFrame(data,dtype=np.float64)
data

#时序图
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
data.plot()
plt.show()

#自相关图
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data).show()

#平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF
print( ADF(data[u'销量']))
#返回值依次为adf、pvalue、usedlag、nobs、critical values、icbest、regresults、resstore

#差分后的结果
D_data = data.diff().dropna()
D_data.columns = [u'销量差分']
D_data.plot() #时序图
plt.show()
plot_acf(D_data).show() #自相关图
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(D_data).show() #偏自相关图
ADF(D_data[u'销量差分'])#平稳性检测

#白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox
acorr_ljungbox(D_data, lags=1) #返回统计量和p值

from statsmodels.tsa.arima_model import ARIMA

#定阶
pmax = int(len(D_data)/10) #一般阶数不超过length/10
qmax = int(len(D_data)/10) #一般阶数不超过length/10
bic_matrix = [] #bic矩阵
for p in range(pmax+1):
  tmp = []
  for q in range(qmax+1):
    try: #存在部分报错，所以用try来跳过报错。
      tmp.append(ARIMA(data, (p,1,q)).fit().bic)
    except:
      tmp.append(None)
  bic_matrix.append(tmp)

bic_matrix = pd.DataFrame(bic_matrix) #从中可以找出最小值

p,q = bic_matrix.stack().idxmin() #先用stack展平，然后用idxmin找出最小值位置。
print(u'BIC最小的p值和q值为：%s、%s' %(p,q)) 
model = ARIMA(data, (0,1,1)).fit() #建立ARIMA(0, 1, 1)模型
model.summary() #给出一份模型报告
model.forecast(5) #作为期5天的预测，返回预测结果、标准误差、置信区间。