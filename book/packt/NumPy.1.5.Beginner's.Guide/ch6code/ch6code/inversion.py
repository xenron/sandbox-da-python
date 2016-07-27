#!/usr/bin/python

import numpy

A = numpy.mat("0 1 2;1 0 3;4 -3 8")
print "A\n", A

inverse = numpy.linalg.inv(A)
print "inverse of A\n", inverse

print "Check\n", A * inverse
