#!/usr/bin/python

import numpy
import sys
from pylab import *

bhp=numpy.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)

vale=numpy.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)

t = numpy.arange(len(bhp))
poly = numpy.polyfit(t, bhp - vale, int(sys.argv[1]))
print "Polynomial fit", poly

print "Next value", numpy.polyval(poly, t[-1] + 1)

print "Roots", numpy.roots(poly)

der = numpy.polyder(poly)
print "Derivative", der

print "Extremas", numpy.roots(der)
vals = numpy.polyval(poly, t)
print numpy.argmax(vals)
print numpy.argmin(vals)

plot(t, bhp - vale)
plot(t, vals)
show()
