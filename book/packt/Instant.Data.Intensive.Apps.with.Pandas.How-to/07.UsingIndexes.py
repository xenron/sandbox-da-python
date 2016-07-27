import numpy as np
import pandas as pd
from pandas.io.data import DataReader



tickers = ['gs', 'ibm', 'f', 'ba', 'axp']
dfs = {}
for ticker in tickers:
    dfs[ticker] = DataReader(ticker, "yahoo", '2006-01-01')

# a yet undiscussed data structure, in the same way the a         # DataFrame is a collection of Series, a Panel is a collection of # DataFrames
pan = pd.Panel(dfs)
pan

pan.items

pan.minor_axis

pan.major_axis
pan.minor_xs('Open').mean()

# major axis is sliceable as well
day_slice = pan.major_axis[1]
pan.major_xs(day_slice)[['gs', 'ba']]


dfs = []
for df in pan:
    idx = pan.major_axis
    idx = pd.MultiIndex.from_tuples(zip([df]*len(idx), idx))
    idx.names = ['ticker', 'timestamp']
    dfs.append(pd.DataFrame(pan[df].values, index=idx,  columns=pan.minor_axis))

df = pd.concat(dfs)

print df

print df.ix['gs':'ibm']
print df['Open']
