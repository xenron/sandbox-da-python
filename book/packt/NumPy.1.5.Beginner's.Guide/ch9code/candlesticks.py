#!/usr/bin/env python

from matplotlib.dates import  DateFormatter, DayLocator, MonthLocator
from matplotlib.finance import quotes_historical_yahoo, candlestick
import sys
from datetime import date
import matplotlib.pyplot as pyplot

today = date.today()
start = (today.year - 1, today.month, today.day)

alldays = DayLocator()              
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

quotes = quotes_historical_yahoo(sys.argv[1], start, today)

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)

candlestick(ax, quotes)
fig.autofmt_xdate()
pyplot.show()


