#!/usr/bin/python

import numpy
import sys

N = int(sys.argv[1])

c = numpy.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

b = c[-N:]
b = b[::-1]
print "b", b

A = numpy.zeros((N, N), float)
print "Zeros N by N", A

for i in range(N):
   A[i, ] = c[-N - 1 - i: - 1 - i]

print "A", A


(x, residuals, rank, s) = numpy.linalg.lstsq(A, b)

print x, residuals, rank, s

print numpy.dot(b, x)
#352.51614809
#actual close 353.56 
