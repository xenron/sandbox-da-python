#!/usr/bin/python

import numpy

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the dtype and shape attributes
# of ndarray.
#
# Run from the commandline with 
#
#  python arrayattributes.py
a = numpy.arange(5)
print "In: a = numpy.arange(5)"

print "In: a.dtype"
print a.dtype
#Out: dtype('int64')
print

print "In: a.shape"
print a.shape
#Out: (5,)
print

print "In: a"
print a
#Out[4]: array([0, 1, 2, 3, 4])
print

m = numpy.array([numpy.arange(2), numpy.arange(2)])

print "In: m"
print m
#Out: 
#array([[0, 1],
#       [0, 1]])
print

print "In: m.shape"
print m.shape
#Out: (2, 2)

print "In: m.dtype"
print m.dtype
#Out: dtype('int64')
print
