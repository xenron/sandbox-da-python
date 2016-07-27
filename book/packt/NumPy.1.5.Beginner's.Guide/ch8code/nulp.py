#!/usr/bin/python

import numpy

eps = numpy.finfo(float).eps
print "EPS", eps
print "1", numpy.testing.assert_array_almost_equal_nulp(1.0, 1.0 + eps)
print "2", numpy.testing.assert_array_almost_equal_nulp(1.0, 1.0 + 2 * eps)

