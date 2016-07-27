#!/usr/bin/python

import numpy

print "Pass", numpy.testing.assert_allclose([0, 0.123456789, numpy.nan], [0, 0.123456780, numpy.nan], rtol=1e-7, atol=0)
print "Fail", numpy.testing.assert_array_equal([0, 0.123456789, numpy.nan], [0, 0.123456780, numpy.nan])
