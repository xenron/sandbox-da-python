#!/usr/bin/python

import numpy
import sys

h, l, c = numpy.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

N = int(sys.argv[1])
h = h[-N:]
l = l[-N:]

print "len(h)", len(h), "len(l)", len(l)
print "Close", c
previousclose = c[-N -1: -1]

print "len(previousclose)", len(previousclose)
print "Previous close", previousclose
truerange = numpy.maximum(h - l, h - previousclose, previousclose - l) 

print "True range", truerange

atr = numpy.zeros(N)

atr[0] = numpy.mean(truerange)

for i in range(1, N):
   atr[i] = (N - 1) * atr[i - 1] + truerange[i]
   atr[i] /= N

print "ATR", atr
