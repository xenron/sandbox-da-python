#!/usr/bin/python

import numpy
from pylab import *

def fit_line(t, y):
   A = numpy.vstack([t, numpy.ones_like(t)]).T

   return numpy.linalg.lstsq(A, y)[0]

h, l, c = numpy.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

pivots = (h + l + c) / 3
print "Pivots", pivots

t = numpy.arange(len(c))
sa, sb = fit_line(t, pivots - (h - l)) 
ra, rb = fit_line(t, pivots + (h - l))

support = sa * t + sb
resistance = ra * t + rb 
condition = (c > support) & (c < resistance)
print "Condition", condition
between_bands = numpy.where(condition) 
print support[between_bands]
print c[between_bands]
print resistance[between_bands]
between_bands = len(numpy.ravel(between_bands))
print "Number points between bands", between_bands
print "Ratio between bands", float(between_bands)/len(c) 

print "Tomorrows support", sa * (t[-1] + 1) + sb
print "Tomorrows resistance", ra * (t[-1] + 1) + rb

a1 = c[c > support]
a2 = c[c < resistance]
print "Number of points between bands 2nd approach" ,len(numpy.intersect1d(a1, a2))

plot(t, c)
plot(t, support)
plot(t, resistance)
show()
