import numpy as np
import pandas as pd

rng = pd.date_range('2000-01-01', '2000-01-05')

tickers = pd.DataFrame(['MSFT', 'AAPL'], columns= ['Ticker'])

df1 = pd.DataFrame({'TickerID': [0]*5,
                   'Price': np.random.normal(100, 10, 5)}, index=rng)

df2 = pd.DataFrame({'TickerID': [1]*5, 'Price': np.random.normal(100, 10, 5)}, index=rng)
print pd.merge(df1, df2, left_index=True, right_index=True)
print pd.merge(df1, tickers, right_index=True, left_on='TickerID')
