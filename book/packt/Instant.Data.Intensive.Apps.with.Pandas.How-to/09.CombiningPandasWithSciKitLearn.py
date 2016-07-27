import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from pandas.io.data import DataReader

tickers = ['gs', 'ibm', 'f', 'ba', 'axp']
dfs = {}
for ticker in tickers:
    dfs[ticker] = DataReader(ticker, "yahoo", '2006-01-01')

# a yet undiscussed data structure, in the same way the a         # DataFrame is a collection of Series, a Panel is a collection of # DataFrames
pan = pd.Panel(dfs)

close = pan.minor_xs('Close')

close.plot()
plt.show()

diff = (close - close.shift(1))
diff = diff[diff < 0].fillna(0)
diff = diff[diff >= 0].fillna(1)
diff.head()

x = diff[['axp', 'ba', 'ibm', 'gs']]
y = diff['f']
obj = svm.SVC()
ft = obj.fit(x, y)
ft

#so given the fit, we can then look at predictions
#all stocks up
ft.predict([1,1,1,1])
#all stocks down
ft.predict([0,0,0,0])
