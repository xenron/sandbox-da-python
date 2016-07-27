#!/usr/bin/python

import numpy

def ultimate_answer(a):
   result = numpy.zeros_like(a)
   result.flat = 42

   return result

ufunc = numpy.frompyfunc(ultimate_answer, 1, 1) 
print "The answer", ufunc(numpy.arange(4))

print "The answer", ufunc(numpy.arange(4).reshape(2, 2))
