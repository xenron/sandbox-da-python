#!/usr/bin/python

from __future__ import division
import numpy

a = numpy.array([2, 6, 5])
b = numpy.array([1, 2, 3])

print "Divide", numpy.divide(a, b), numpy.divide(b, a)
print "True Divide", numpy.true_divide(a, b), numpy.true_divide(b, a)
print "Floor Divide", numpy.floor_divide(a, b), numpy.floor_divide(b, a)
c = 3.14 * b
print "Floor Divide 2", numpy.floor_divide(c, b), numpy.floor_divide(b, c)
print "/ operator", a/b, b/a
print "// operator", a//b, b//a
print "// operator 2", c//b, b//c
