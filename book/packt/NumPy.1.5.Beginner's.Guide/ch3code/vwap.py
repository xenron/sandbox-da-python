#!/usr/bin/python

import numpy

c,v=numpy.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
vwap = numpy.average(c, weights=v)
print "VWAP =", vwap

print "mean =", numpy.mean(c)

t = numpy.arange(len(c))
print "twap =", numpy.average(c, weights=t)
