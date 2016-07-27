import numpy as np
import pandas as pd
from pandas.io.data import DataReader
import matplotlib.pyplot as plt


tickers = ['gs', 'ibm', 'f', 'ba', 'axp']
dfs = {}
for ticker in tickers:
    dfs[ticker] = DataReader(ticker, "yahoo", '2006-01-01')

# a yet undiscussed data structure, in the same way the a         # DataFrame is a collection of Series, a Panel is a collection of # DataFrames
pan = pd.Panel(dfs)

close = pan.minor_xs('Close')

close.mean().plot(kind='bar')
plt.show()
