#!/usr/bin/python

import numpy

x = numpy.arange(-9, 9)
y = -x
print "Sign different?", (x ^ y) < 0
print "Sign different?", numpy.less(numpy.bitwise_xor(x, y), 0)
print "Power of 2?\n", x, "\n", (x & (x - 1)) == 0
print "Power of 2?\n", x, "\n", numpy.equal(numpy.bitwise_and(x,  (x - 1)), 0)
print "Modulus 4\n", x, "\n", x & ((1 << 2) - 1)
print "Modulus 4\n", x, "\n", numpy.bitwise_and(x, numpy.left_shift(1, 2) - 1)
