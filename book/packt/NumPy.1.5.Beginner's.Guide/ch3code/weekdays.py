#!/usr/bin/python

import numpy
from datetime import datetime

# Monday 0
# Tuesday 1
# Wednesday 2
# Thursday 3
# Friday 4
# Saturday 5
# Sunday 6
def datestr2num(s):
   return datetime.strptime(s, "%d-%m-%Y").date().weekday()

dates, close=numpy.loadtxt('data.csv', delimiter=',', usecols=(1,6), converters={1: datestr2num}, unpack=True)
print "Dates =", dates

averages = numpy.zeros(5)

for i in range(5):
   indices = numpy.where(dates == i) 
   prices = numpy.take(close, indices)
   avg = numpy.mean(prices)
   print "Day", i, "prices", prices, "Average", avg
   averages[i] = avg


top = numpy.max(averages)
print "Highest average", top
print "Top day of the week", numpy.argmax(averages)

bottom = numpy.min(averages)
print "Lowest average", bottom
print "Bottom day of the week", numpy.argmin(averages)

