import pandas
from matplotlib.pyplot import show, legend
from datetime import datetime
from matplotlib import finance
import numpy

# Download AAPL data for 2011 to 2012
start = datetime(2011, 01, 01)
end = datetime(2012, 01, 01)

symbol = "AAPL"
quotes = finance.quotes_historical_yahoo(symbol, start, end, asobject=True)

# Create date time index
dt_idx = pandas.DatetimeIndex(quotes.date)

#Create data frame
df = pandas.DataFrame(quotes.close, index=dt_idx, columns=[symbol])

# Resample with monthly frequency
resampled = df.resample('M', how=numpy.mean)
print resampled 
 
# Plot
df.plot()
resampled.plot()
show()
