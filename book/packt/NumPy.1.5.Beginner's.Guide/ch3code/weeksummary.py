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

dates, open, high, low, close=numpy.loadtxt('data.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), converters={1: datestr2num}, unpack=True)
close = close[:16]
dates = dates[:16]

# get first Monday
first_monday = numpy.ravel(numpy.where(dates == 0))[0]
print "The first Monday index is", first_monday

# get last Friday
last_friday = numpy.ravel(numpy.where(dates == 4))[-1]
print "The last Friday index is", last_friday

weeks_indices = numpy.arange(first_monday, last_friday + 1)
print "Weeks indices initial", weeks_indices

weeks_indices = numpy.split(weeks_indices, 3)
print "Weeks indices after split", weeks_indices

def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = numpy.max( numpy.take(h, a) )
    week_low = numpy.min( numpy.take(l, a) )
    friday_close = c[a[-1]]

    return("APPL", monday_open, week_high, week_low, friday_close)

weeksummary = numpy.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print "Week summary", weeksummary

numpy.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")
