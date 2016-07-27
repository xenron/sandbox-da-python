#!/usr/bin/python

import numpy
import sys
from pylab import *

N = int(sys.argv[1])

weights = numpy.ones(N) / N
print "Weights", weights

c = numpy.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = numpy.convolve(weights, c)[N-1:-N+1]
deviation = []
C = len(c)

for i in range(N - 1, C):
   if i + N < C:
      dev = c[i: i + N]
   else:
      dev = c[-N:]
   
   averages = numpy.zeros(N)
   averages.fill(sma[i - N - 1])
   dev = dev - averages 
   dev = dev ** 2
   dev = numpy.sqrt(numpy.mean(dev))
   deviation.append(dev)

deviation = 2 * numpy.array(deviation)
print len(deviation), len(sma)
upperBB = sma + deviation
lowerBB = sma - deviation

c_slice = c[N-1:]
between_bands = numpy.where((c_slice < upperBB) & (c_slice > lowerBB))

print lowerBB[between_bands]
print c[between_bands]
print upperBB[between_bands]
between_bands = len(numpy.ravel(between_bands))
print "Ratio between bands", float(between_bands)/len(c_slice)

t = numpy.arange(N - 1, C)
plot(t, c_slice, lw=1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()
