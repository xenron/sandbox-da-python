#!/usr/bin/python

import numpy

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy numerical types
#  and conversion between them.
#
# Run from the commandline with 
#
#  python numericaltypes.py

print "In: float64(42)"
print numpy.float64(42)
#Out: 42.0

print "In: int8(42.0)"
print numpy.int8(42.0)
#Out: 42

print "In: bool(42)"
print numpy.bool(42)
#Out: True

print "In: bool(42.0)"
print numpy.bool(42.0)
#Out: True

print "In: float(True)"
print numpy.float(True)
#Out: 1.0

print "In: arange(7, dtype=uint16)"
print numpy.arange(7, dtype=numpy.uint16)
#Out: array([0, 1, 2, 3, 4, 5, 6], dtype=uint16)


print "In: int(42.0 + 1.j)"
try:
   print numpy.int(42.0 + 1.j)
except TypeError:
   print "TypeError"
#Type error

print "In: float(42.0 + 1.j)"
print float(42.0 + 1.j)
#Type error
