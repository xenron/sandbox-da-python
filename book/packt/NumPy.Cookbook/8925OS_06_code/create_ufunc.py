import numpy

def double(a):
   return 2 * a

ufunc = numpy.frompyfunc(double, 1, 1)
print "Result", ufunc(numpy.arange(4))
