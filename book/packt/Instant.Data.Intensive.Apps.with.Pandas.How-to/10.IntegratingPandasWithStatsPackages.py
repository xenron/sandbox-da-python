import numpy as np
from pandas.io.data import DataReader
import pandas as pd
import statsmodels.api as sm


tickers = ['gs', 'ibm', 'f', 'ba', 'axp']
dfs = {}
for ticker in tickers:
    dfs[ticker] = DataReader(ticker, "yahoo", '2006-01-01')

pan = pd.Panel(dfs)

close = pan.minor_xs('Close')


x = close[['axp', 'ba', 'gs', 'ibm']]
y = close['f']
ols_model = sm.OLS(y,x)
fit = ols_model.fit()
fit.t()
fit.conf_int()
