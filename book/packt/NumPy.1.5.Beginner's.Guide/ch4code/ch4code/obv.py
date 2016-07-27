#!/usr/bin/python

import numpy

c, v=numpy.loadtxt('BHP.csv', delimiter=',', usecols=(6, 7), unpack=True)

change = numpy.diff(c)
print "Change", change

signs = numpy.sign(change)
print "Signs", signs

pieces = numpy.piecewise(change, [change < 0, change > 0], [-1, 1])
print "Pieces", pieces

print "Arrays equal?", numpy.array_equal(signs, pieces)

print "On balance volume", v[1:] * signs

