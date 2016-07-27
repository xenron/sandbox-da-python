#!/usr/bin/python

import numpy
import sys
from pylab import *

x = numpy.arange(5)
print "Exp", numpy.exp(x)
print "Linspace", numpy.linspace(-1, 0, 5)

N = int(sys.argv[1])


weights = numpy.exp(numpy.linspace(-1., 0., N))
weights /= weights.sum()
print "Weights", weights

c = numpy.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = numpy.convolve(weights, c)[N-1:-N+1]
t = numpy.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, ema, lw=2.0)
show()
