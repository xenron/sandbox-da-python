#!/usr/bin/python

import numpy

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates array stacking.
#
# Run from the commandline with 
#
#  python stacking.py
print "In: a = arange(9).reshape(3,3)"
a = numpy.arange(9).reshape(3,3)

print "In: a"
print a
#Out: 
#array([[0, 1, 2],
#       [3, 4, 5],
#       [6, 7, 8]])

print "In: b = 2 * a"
b = 2 * a

print "In: b"
print b
#Out: 
#array([[ 0,  2,  4],
#       [ 6,  8, 10],
#       [12, 14, 16]])

print "In: hstack((a, b))"
print numpy.hstack((a, b))
#Out: 
#array([[ 0,  1,  2,  0,  2,  4],
#       [ 3,  4,  5,  6,  8, 10],
#       [ 6,  7,  8, 12, 14, 16]])

print "In: concatenate((a, b), axis=1)"
print numpy.concatenate((a, b), axis=1)
#Out: 
#array([[ 0,  1,  2,  0,  2,  4],
#       [ 3,  4,  5,  6,  8, 10],
#       [ 6,  7,  8, 12, 14, 16]])

print "In: vstack((a, b))"
print numpy.vstack((a, b))
#Out: 
#array([[ 0,  1,  2],
#       [ 3,  4,  5],
#       [ 6,  7,  8],
#       [ 0,  2,  4],
#       [ 6,  8, 10],
#       [12, 14, 16]])

print "In: concatenate((a, b), axis=0)"
print numpy.concatenate((a, b), axis=0)
#Out: 
#array([[ 0,  1,  2],
#       [ 3,  4,  5],
#       [ 6,  7,  8],
#       [ 0,  2,  4],
#       [ 6,  8, 10],
#       [12, 14, 16]])

print "In: dstack((a, b))"
print numpy.dstack((a, b))
#Out: 
#array([[[ 0,  0],
#        [ 1,  2],
#        [ 2,  4]],
#
#       [[ 3,  6],
#        [ 4,  8],
#        [ 5, 10]],
#
#       [[ 6, 12],
#        [ 7, 14],
#        [ 8, 16]]])

print "In: oned = arange(2)"
oned = numpy.arange(2)

print "In: oned"
print oned
#Out: array([0, 1])

print "In: twiceoned = 2 * oned"
twiceoned = 2 * oned

print "In: twiceoned"
print twiceoned
#Out: array([0, 2])

print "In: column_stack((oned, twiceoned))"
print numpy.column_stack((oned, twiceoned)) 
#Out: 
#array([[0, 0],
#       [1, 2]])

print "In: column_stack((a, b))"
print numpy.column_stack((a, b))
#Out: 
#array([[ 0,  1,  2,  0,  2,  4],
#       [ 3,  4,  5,  6,  8, 10],
#       [ 6,  7,  8, 12, 14, 16]])

print "In: column_stack((a, b)) == hstack((a, b))"
print numpy.column_stack((a, b)) == numpy.hstack((a, b))
#Out: 
#array([[ True,  True,  True,  True,  True,  True],
#       [ True,  True,  True,  True,  True,  True],
#       [ True,  True,  True,  True,  True,  True]], dtype=bool)

print "In: row_stack((oned, twiceoned))"
print numpy.row_stack((oned, twiceoned))
#Out: 
#array([[0, 1],
#       [0, 2]])
 
print "In: row_stack((a, b))"
print numpy.row_stack((a, b))
#Out: 
#array([[ 0,  1,  2],
#       [ 3,  4,  5],
#       [ 6,  7,  8],
#       [ 0,  2,  4],
#       [ 6,  8, 10],
#       [12, 14, 16]])

print "In: row_stack((a,b)) == vstack((a, b))"
print numpy.row_stack((a,b)) == numpy.vstack((a, b))
#Out: 
#array([[ True,  True,  True],
#       [ True,  True,  True],
#       [ True,  True,  True],
#       [ True,  True,  True],
#       [ True,  True,  True],
#       [ True,  True,  True]], dtype=bool)

