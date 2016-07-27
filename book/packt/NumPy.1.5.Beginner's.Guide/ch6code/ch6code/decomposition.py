#!/usr/bin/python

import numpy

A = numpy.mat("4 11 14;8 7 -2")
print "A\n", A

U, Sigma, V = numpy.linalg.svd(A, full_matrices=False)

print "U"
print U

print "Sigma"
print Sigma

print "V"
print V

print "Product\n", U * numpy.diag(Sigma) * V
