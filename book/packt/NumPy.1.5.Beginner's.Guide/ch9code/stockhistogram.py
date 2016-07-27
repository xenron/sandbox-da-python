#!/usr/bin/env python

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

pyplot.hist(close, numpy.sqrt(len(close)))
pyplot.show()
