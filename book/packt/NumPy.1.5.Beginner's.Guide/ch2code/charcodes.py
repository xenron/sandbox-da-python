#!/usr/bin/python

import numpy

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy dtype character codes.
#
# Run from the commandline with 
#
#  python charcodes.py

print "In: arange(7, dtype='f')"
print numpy.arange(7, dtype='f')
#Out: array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.], dtype=float32)

print "In: arange(7, dtype='D')"
print numpy.arange(7, dtype='D')
#Out: array([ 0.+0.j,  1.+0.j,  2.+0.j,  3.+0.j,  4.+0.j,  5.+0.j,  6.+0.j])


