#!/usr/bin/python

import numpy
import sys
from pylab import *

N = int(sys.argv[1])

weights = numpy.ones(N) / N
print "Weights", weights

c = numpy.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = numpy.convolve(weights, c)[N-1:-N+1]
t = numpy.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, sma, lw=2.0)
show()
