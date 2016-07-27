#!/usr/bin/python

import numpy

print "Decimal 8", numpy.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=8)
print "Decimal 9", numpy.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=9)

