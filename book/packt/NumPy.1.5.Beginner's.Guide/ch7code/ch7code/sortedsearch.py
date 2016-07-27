#!/usr/bin/python

import numpy

a = numpy.arange(5)
indices = numpy.searchsorted(a, [-2, 7])
print "Indices", indices

print "The full array", numpy.insert(a, indices, [-2, 7])
