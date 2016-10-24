# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 10:32:08 2016

@author: Administrator
"""

###欧式看涨期权的蒙特卡洛估值
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

from numpy import *

I = 100000

random.seed(1000)
z = random.standard_normal(I)
ST = S0 * exp(r * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
C0 = exp(-r * T) * sum(hT) / I

print "Value of the European Call Option %5.3f" % C0

###可视化

import numpy as np
import pandas as pd


xlsx_file = pd.ExcelFile("d:\data\stockprice.xlsx")
djia=xlsx_file.parse('DJIA')
djia.tail()

djia['Log_Ret'] = np.log(djia['Close'] / djia['Close'].shift(1))
djia['Volatility'] = djia['Log_Ret'].rolling(window=100,center=False).std()

get_ipython().magic('matplotlib inline')
djia[['Close', 'Volatility']].plot(subplots=True, color='blue',
                                   figsize=(8, 6), grid=True);
                                   
                        
###高性能计算
loops = 25000000
from math import *
a = range(1, loops)
def f(x):
    return 3 * log(x) + cos(x) ** 2
get_ipython().magic('timeit r = [f(x) for x in a]')


import numpy as np
a = np.arange(1, loops)
get_ipython().magic('timeit r = 3 * np.log(a) + np.cos(a) ** 2')


import numexpr as ne
ne.set_num_threads(1)
f = '3 * log(a) + cos(a) ** 2'
get_ipython().magic('timeit r = ne.evaluate(f)')
                   