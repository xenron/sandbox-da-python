#!/usr/bin/python

import numpy

print "Pass", numpy.testing.assert_string_equal("NumPy", "NumPy")
print "Fail", numpy.testing.assert_string_equal("NumPy", "Numpy")
