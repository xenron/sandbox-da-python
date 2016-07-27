#!/usr/bin/python

import numpy

print "Pass", numpy.testing.assert_array_less([0, 0.123456789, numpy.nan], [1, 0.23456780, numpy.nan])
print "Fail", numpy.testing.assert_array_less([0, 0.123456789, numpy.nan], [0, 0.123456780, numpy.nan])

