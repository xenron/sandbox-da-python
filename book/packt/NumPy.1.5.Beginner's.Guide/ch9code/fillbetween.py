#!/usr/bin/env python

from matplotlib.finance import quotes_historical_yahoo
from matplotlib.dates import  DateFormatter, DayLocator, MonthLocator
import sys
from datetime import date
import matplotlib.pyplot as pyplot
import numpy

today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo(sys.argv[1], start, today)
quotes = numpy.array(quotes)
dates = quotes.T[0]
close = quotes.T[4]


alldays = DayLocator()              
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.plot(dates, close) 
pyplot.fill_between(dates, close.min(), close, where=close>close.mean(), facecolor="green", alpha=0.4)
pyplot.fill_between(dates, close.min(), close, where=close<close.mean(), facecolor="red", alpha=0.4)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
pyplot.show()
