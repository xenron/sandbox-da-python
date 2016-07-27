#!/usr/bin/python

import numpy

A = numpy.mat("1 -2 1;0 2 -8;-4 5 9")
print "A\n", A

b = numpy.array([0, 8, -9])
print "b\n", b

x = numpy.linalg.solve(A, b)
print "Solution", x

print "Check\n", numpy.dot(A , x)
