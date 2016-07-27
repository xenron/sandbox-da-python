#!/usr/bin/python

import numpy

a = numpy.arange(-4, 4)

print "Remainder", numpy.remainder(a, 2)
print "Mod", numpy.mod(a, 2)
print "% operator", a % 2
print "Fmod", numpy.fmod(a, 2)
