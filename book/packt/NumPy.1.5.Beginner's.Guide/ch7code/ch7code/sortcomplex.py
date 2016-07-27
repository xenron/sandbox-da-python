#!/usr/bin/python

import numpy

numpy.random.seed(42)
complex_numbers = numpy.random.random(5) + 1j * numpy.random.random(5)
print "Complex numbers\n", complex_numbers

print "Sorted\n", numpy.sort_complex(complex_numbers)
