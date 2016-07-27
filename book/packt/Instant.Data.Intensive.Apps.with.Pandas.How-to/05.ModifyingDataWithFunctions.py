import pandas as pd
import numpy as np

data = {'Open': np.random.normal(100, 5, 366),
                 'Close': np.random.normal(100, 5, 366)}

df = pd.DataFrame(data)

print df
df.apply(np.mean, axis=1).head(3)

#passing a lambda is a common pattern
df.apply(lambda x: (x['Open'] - x['Close']), axis=1).head(3)
#define a more complex function
def percent_change(x):
    return (x['Open'] - x['Close']) / x['Open']

print df.apply(percent_change, axis=1).head(3)

#change axis, axis = 0 is default
print df.apply(np.mean, axis=0)

def greater_than_x(element, x):
    return element > x

print df.Open.apply(greater_than_x, args=(100,)).head(3)

#This can be used as in conjunction with subset capabilities
mask = df.Open.apply(greater_than_x, args=(100,))

print df.Open[mask].head()

print pd.rolling_apply(df.Close, 5, np.mean)

#There are actually a several built-in rolling functions
print pd.rolling_corr(df.Close, df.Open, 5)[:5]
