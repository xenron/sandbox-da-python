#!/usr/bin/python

import numpy

print "Decimal 6", numpy.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=7)
print "Decimal 7", numpy.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=8)
