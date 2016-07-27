#!/usr/bin/python

import numpy

F = numpy.matrix([[1, 1], [1, 0]])
print "F", F
print "8th Fibonacci", (F ** 7)[0, 0]
n = numpy.arange(1, 9)

sqrt5 = numpy.sqrt(5)
phi = (1 + sqrt5)/2
fibonacci = numpy.rint((phi**n - (-1/phi)**n)/sqrt5)
print "Fibonacci", fibonacci


