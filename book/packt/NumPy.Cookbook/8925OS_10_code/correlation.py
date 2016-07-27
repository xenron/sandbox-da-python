import pandas
from matplotlib.pyplot import show, legend
from datetime import datetime
from matplotlib import finance
import numpy

# 2011 to 2012
start = datetime(2011, 01, 01)
end = datetime(2012, 01, 01)

symbols = ["AA", "AXP", "BA", "BAC", "CAT"]

quotes = [finance.quotes_historical_yahoo(symbol, start, end, asobject=True)
          for symbol in symbols]

close = numpy.array([q.close for q in quotes]).astype(numpy.float)
dates = numpy.array([q.date for q in quotes])

data = {}

for i in xrange(len(symbols)):
   data[symbols[i]] = numpy.diff(numpy.log(close[i]))

df = pandas.DataFrame(data, index=dates[0][:-1], columns=symbols)
 
 
print df.corr()
df.plot()
legend(symbols)
show()

#           AA       AXP        BA       BAC       CAT
#AA   1.000000  0.768484  0.758264  0.737625  0.837643
#AXP  0.768484  1.000000  0.746898  0.760043  0.736337
#BA   0.758264  0.746898  1.000000  0.657075  0.770696
#BAC  0.737625  0.760043  0.657075  1.000000  0.657113
#CAT  0.837643  0.736337  0.770696  0.657113  1.000000
