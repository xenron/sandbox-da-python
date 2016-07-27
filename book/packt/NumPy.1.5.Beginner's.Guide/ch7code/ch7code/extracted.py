#!/usr/bin/python

import numpy

a = numpy.arange(7)
condition = (a % 2) == 0
print "Even numbers", numpy.extract(condition, a)
