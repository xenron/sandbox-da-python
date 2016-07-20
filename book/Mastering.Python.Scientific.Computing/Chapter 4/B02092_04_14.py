import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('apple-data.csv', index_col = 'Date', parse_dates=True)
df['H-L'] = df.High - df.Low
df['50MA'] = pd.rolling_mean(df['Close'], 50)
df[['Open','High','Low','Close','50MA']].plot()
plt.show()