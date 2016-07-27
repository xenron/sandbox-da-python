#!/usr/bin/python

import numpy

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy dtype constructors.
#
# Run from the commandline with 
#
#  python dtypeconstructors.py
print "In: dtype(float)"
print numpy.dtype(float)
#Out: dtype('float64')

print "In: dtype('f')"
print numpy.dtype('f')
#Out: dtype('float32')


print "In: dtype('d')"
print numpy.dtype('d')
#Out: dtype('float64')

print "In: dtype('f8')"
print numpy.dtype('f8')
#Out: dtype('float64')


print "In: dtype('Float64')"
print numpy.dtype('Float64')
#Out: dtype('float64')

