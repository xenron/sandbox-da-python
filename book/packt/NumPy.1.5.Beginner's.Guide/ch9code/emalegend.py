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


fig = pyplot.figure()
ax = fig.add_subplot(111)

emas = []
for i in range(9, 18, 3):
   weights = numpy.exp(numpy.linspace(-1., 0., i))
   weights /= weights.sum()

   ema = numpy.convolve(weights, close)[i-1:-i+1]
   idx = (i - 6)/3
   ax.plot(dates[i-1:], ema, lw=idx, label="EMA(%s)" % (i))
   data = numpy.column_stack((dates[i-1:], ema))
   emas.append(numpy.rec.fromrecords(data, names=["dates", "ema"]))   

first = emas[0]["ema"].flatten() 
second = emas[1]["ema"].flatten()
bools = numpy.abs(first[-len(second):] - second)/second < 0.0001
xpoints = numpy.compress(bools, emas[1])

for xpoint in xpoints:
   ax.annotate('x', xy=xpoint, textcoords='offset points',
                xytext=(-50, 30),
                arrowprops=dict(arrowstyle="->"))
   
leg = ax.legend(loc='best', fancybox=True)
leg.get_frame().set_alpha(0.5)

alldays = DayLocator()              
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
ax.plot(dates, close, lw=1.0, label="Close")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
pyplot.show()
