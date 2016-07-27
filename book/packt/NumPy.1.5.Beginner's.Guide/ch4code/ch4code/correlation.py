#!/usr/bin/python

import numpy
from pylab import *

bhp = numpy.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)

bhp_returns = numpy.diff(bhp) / bhp[ : -1]

vale = numpy.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)

vale_returns = numpy.diff(vale) / vale[ : -1]

covariance = numpy.cov(bhp_returns, vale_returns) 
print "Covariance", covariance

print "Covariance diagonal", covariance.diagonal()
print "Covariance trace", covariance.trace()

print covariance/ (bhp_returns.std() * vale_returns.std())

print "Correlation coefficient", numpy.corrcoef(bhp_returns, vale_returns)

difference = bhp - vale
avg = numpy.mean(difference)
dev = numpy.std(difference)

print "Out of sync", numpy.abs(difference[-1] - avg) > 2 * dev

t = numpy.arange(len(bhp_returns))
plot(t, bhp_returns, lw=1)
plot(t, vale_returns, lw=2)
show()
