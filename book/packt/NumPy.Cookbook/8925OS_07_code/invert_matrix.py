import numpy

def invert(n):
   a = numpy.matrix(numpy.random.rand(n, n))
   return a.I

sizes = 2 ** numpy.arange(0, 12)

for n in sizes:
   invert(n)
