#!/usr/bin/python

import numpy

A = numpy.mat("3 4;5 6")
print "A\n", A

print "Determinant", numpy.linalg.det(A)
