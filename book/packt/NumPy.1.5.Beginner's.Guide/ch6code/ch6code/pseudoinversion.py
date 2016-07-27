#!/usr/bin/python

import numpy

A = numpy.mat("4 11 14;8 7 -2")
print "A\n", A

pseudoinv = numpy.linalg.pinv(A)
print "Pseudo inverse\n", pseudoinv

print "Check", A * pseudoinv
