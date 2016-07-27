#!/usr/bin/python

import numpy

a = numpy.arange(9)

print "Reduce", numpy.add.reduce(a)
print "Accumulate", numpy.add.accumulate(a)
print "Reduceat", numpy.add.reduceat(a, [0, 5, 2, 7])
print "Reduceat step I", numpy.add.reduce(a[0:5])
print "Reduceat step II", a[5]
print "Reduceat step III", numpy.add.reduce(a[2:7])
print "Reduceat step IV", numpy.add.reduce(a[7:])
print "Outer", numpy.add.outer(numpy.arange(3), a)
