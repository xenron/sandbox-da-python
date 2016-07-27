#!/usr/bin/python

import numpy

print "Significance 8", numpy.testing.assert_approx_equal(0.123456789, 0.123456780, significant=8)
print "Significance 9", numpy.testing.assert_approx_equal(0.123456789, 0.123456780, significant=9)

