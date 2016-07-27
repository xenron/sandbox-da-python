#!/usr/bin/python

import numpy
import sys
from pylab import *

N = int(sys.argv[1])

weights = numpy.hanning(N)
print "Weights", weights

bhp = numpy.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
bhp_returns = numpy.diff(bhp) / bhp[ : -1]
smooth_bhp = numpy.convolve(weights/weights.sum(), bhp_returns)[N-1:-N+1]

vale = numpy.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)
vale_returns = numpy.diff(vale) / vale[ : -1]
smooth_vale = numpy.convolve(weights/weights.sum(), vale_returns)[N-1:-N+1]

K = int(sys.argv[1])
t = numpy.arange(N - 1, len(bhp_returns))
poly_bhp = numpy.polyfit(t, smooth_bhp, K)
poly_vale = numpy.polyfit(t, smooth_vale, K)

poly_sub = numpy.polysub(poly_bhp, poly_vale)
xpoints = numpy.roots(poly_sub)
print "Intersection points", xpoints

reals = numpy.isreal(xpoints)
print "Real number?", reals

xpoints = numpy.select([reals], [xpoints])
xpoints = xpoints.real
print "Real intersection points", xpoints

print "Sans 0s", numpy.trim_zeros(xpoints)

plot(t, bhp_returns[N-1:], lw=1.0)
plot(t, smooth_bhp, lw=2.0)

plot(t, vale_returns[N-1:], lw=1.0)
plot(t, smooth_vale, lw=2.0)
show()
