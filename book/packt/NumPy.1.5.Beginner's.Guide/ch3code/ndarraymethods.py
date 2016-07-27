#!/usr/bin/python

import numpy

a = numpy.arange(5)
print "a =", a
print "Clipped", a.clip(1, 2)

a = numpy.arange(4)
print a
print "Compressed", a.compress(a > 2)

b = numpy.arange(1, 9)
print "b =", b
print "Factorial", b.prod()

print "Factorials", b.cumprod()
