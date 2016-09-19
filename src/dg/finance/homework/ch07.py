# -*- coding: utf-8 -*-
# 利用stock_px.csv中的股票数据，构造出最佳的投资组合

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import math
import scipy.stats as scs
import pandas.io.data as web
import scipy.optimize as sco

# 读取数据
data = pd.read_csv('d:/tmp/stock_px.csv', parse_dates=True, index_col=0)
data.plot(figsize=(8, 4), grid=True)
# 归一化数据
(data / data.ix[0] * 100).plot(figsize=(8, 4), grid=True)
noa = len(data.columns)

# 投资组合优化
def statistics(weights,rf=0):
    ''' Return portfolio statistics.
    
    Parameters
    ==========
    weights : array-like
        weights for different securities in portfolio
    
    Returns
    =======
    pret : float
        expected portfolio return
    pvol : float
        expected portfolio volatility
    pret / pvol : float
        Sharpe ratio for rf=0
    '''
    weights = np.array(weights)
    pret = np.sum(rets.mean() * weights) * 252
    pvol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
    return np.array([pret, pvol, (pret-rf) / pvol])

############################ sharpe值最大 ############################

def min_func_sharpe(weights):
    return -statistics(weights)[2]

cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})

bnds = tuple((0, 1) for x in range(noa))

noa * [1. / noa,]

get_ipython().run_cell_magic(u'time', u'', u"opts = sco.minimize(min_func_sharpe, noa * [1. / noa,], method='SLSQP', bounds=bnds, constraints=cons)")

opts

opts['x'].round(3)

statistics(opts['x']).round(3)

############################ 方差最小 ############################

def min_func_variance(weights):
    return statistics(weights)[1] ** 2

optv = sco.minimize(min_func_variance, noa * [1. / noa,], method='SLSQP',
                       bounds=bnds, constraints=cons)

optv

optv['x'].round(3)

statistics(optv['x']).round(3)


