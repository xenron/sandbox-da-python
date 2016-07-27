#!/usr/bin/python

import numpy

h,l=numpy.loadtxt('data.csv', delimiter=',', usecols=(4,5), unpack=True)
print "highest =", numpy.max(h)
print "lowest =", numpy.min(l)
print (numpy.max(h) + numpy.min(l)) /2

print "Spread high price", numpy.ptp(h)
print "Spread low price", numpy.ptp(l)
