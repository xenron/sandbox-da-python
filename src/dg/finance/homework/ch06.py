# -*- coding: utf-8 -*-

# 数据集：第4周的stock_px.csv
# 1. 计算苹果公司每天的简单收益率和对数收益率
# 2. 检验苹果公司 两个收益率的正态性
# 3. 检验苹果公司股价和对数股价的正态性


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import math
import scipy.stats as scs
##时间序列可视化


#简单收益率
def ret(pt,p0):
    print '简单收益率为'+str((pt-p0)/p0*100)+'%'
    return (pt-p0)/p0

#对数收益率
def log_ret(pt,p0):
#    return math.log(pt/p0)
    return np.log(pt/p0)

close_px_all = pd.read_csv('d:/tmp/stock_px.csv', parse_dates=True, index_col=0)
aapl_stock = close_px_all[['AAPL']]
aapl_stock.columns =['price']
#close_px = close_px.resample('B').ffill()
#close_px.info()
#close_px['diff'] = close_px.diff()
#df_yesterday = DataFrame(data=close_px[:-1], index=close_px.index.values)
#previous_price = close_px.shift(1)
aapl_stock['previous']=aapl_stock.shift(1)
aapl_stock['log_price']=np.log(aapl_stock['price'])
aapl_stock['ret']=ret(aapl_stock['price'], aapl_stock['previous'])
aapl_stock['log_ret']=log_ret(aapl_stock['price'],aapl_stock['previous'])

def normality_tests(arr):
    ''' Tests for normality distribution of given data set.
    
    Parameters
    ==========
    array: ndarray
        object to generate statistics on
    '''
    print "Skew of data set  %14.3f" % scs.skew(arr)
    print "Skew test p-value %14.3f" % scs.skewtest(arr)[1]
    print "Kurt of data set  %14.3f" % scs.kurtosis(arr)
    print "Kurt test p-value %14.3f" % scs.kurtosistest(arr)[1]
    print "Norm test p-value %14.3f" % scs.normaltest(arr)[1]

normality_tests(aapl_stock['ret'][1:])
normality_tests(aapl_stock['log_ret'][1:])

normality_tests(aapl_stock['price'])
normality_tests(aapl_stock['log_price'])
