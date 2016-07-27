#!/usr/bin/python

import numpy
import datetime

def datestr2num(s):
   return datetime.datetime.strptime(s, "%d-%m-%Y").toordinal()

dates,closes=numpy.loadtxt('AAPL.csv', delimiter=',', usecols=(1, 6), converters={1:datestr2num}, unpack=True)
indices = numpy.lexsort((dates, closes))

print "Indices", indices
print ["%s %s" % (datetime.date.fromordinal(dates[i]),  closes[i]) for i in indices]
