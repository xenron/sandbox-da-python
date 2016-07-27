#!/usr/bin/python

import numpy

A = numpy.eye(2)
print "A", A
B = 2 * A
print "B", B
print "Compound matrix\n", numpy.bmat("A B; A B")

