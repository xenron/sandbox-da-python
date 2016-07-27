#!/usr/bin/python

import numpy

c=numpy.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

returns = numpy.diff( c ) / c[ : -1]
print "Standard deviation =", numpy.std(returns)

logreturns = numpy.diff( numpy.log(c) )

posretindices = numpy.where(returns > 0)
print "Indices with positive returns", posretindices

annual_volatility = numpy.std(logreturns)/numpy.mean(logreturns)
annual_volatility = annual_volatility / numpy.sqrt(1./252.)
print "Annual volatility", annual_volatility

print "Monthly volatility", annual_volatility * numpy.sqrt(1./12.)
