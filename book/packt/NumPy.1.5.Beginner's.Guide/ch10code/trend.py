#!/usr/bin/env python

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import scipy.signal
import matplotlib.pyplot
from matplotlib.dates import  DateFormatter, DayLocator, MonthLocator


today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo("QQQ", start, today)
quotes = numpy.array(quotes)

dates = quotes.T[0]
qqq = quotes.T[4]


y = scipy.signal.detrend(qqq)

alldays = DayLocator()              
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)

matplotlib.pyplot.plot(dates, qqq, 'o', dates, qqq - y, '-')
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)
fig.autofmt_xdate()
matplotlib.pyplot.show()
