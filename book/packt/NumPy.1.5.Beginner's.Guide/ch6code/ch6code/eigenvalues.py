#!/usr/bin/python

import numpy

A = numpy.mat("3 -2;1 0")
print "A\n", A

print "Eigenvalues", numpy.linalg.eigvals(A)

eigenvalues, eigenvectors = numpy.linalg.eig(A)
print "First tuple of eig", eigenvalues
print "Second tuple of eig\n", eigenvectors

for i in range(len(eigenvalues)):
   print "Left", numpy.dot(A, eigenvectors[:,i])
   print "Right", eigenvalues[i] * eigenvectors[:,i]
   print
