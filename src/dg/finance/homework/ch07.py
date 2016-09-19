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

