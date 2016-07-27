import numpy
import cProfile
import sys

def transpose(n):
   random_values = numpy.random.random((n, n))
   return random_values.T

cProfile.run('transpose(%d)' %(int(sys.argv[1])))
