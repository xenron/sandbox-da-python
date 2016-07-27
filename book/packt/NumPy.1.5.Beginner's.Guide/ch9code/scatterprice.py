from matplotlib.finance import quotes_historical_yahoo
import sys
from datetime import date
import matplotlib.pyplot as pyplot
import numpy

today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo(sys.argv[1], start, today)
quotes = numpy.array(quotes)
close = quotes.T[4]
volume = quotes.T[5]
ret = numpy.diff(close)/close[:-1]
volchange = numpy.diff(volume)/volume[:-1]

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.scatter(ret, volchange, c=ret * 100, s=volchange * 100, alpha=0.5)
ax.set_title('Close and volume returns')
ax.grid(True)

pyplot.show()

