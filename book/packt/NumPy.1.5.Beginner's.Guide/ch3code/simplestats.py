#!/usr/bin/python

import numpy

c=numpy.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print "median =", numpy.median(c)
sorted = numpy.msort(c)
print "sorted =", sorted

N = len(c)
print "middle =", sorted[(N - 1)/2]
print "average middle =", (sorted[N /2] + sorted[(N - 1) / 2]) / 2

print "variance =", numpy.var(c)
print "variance from definition =", numpy.mean((c - c.mean())**2)
