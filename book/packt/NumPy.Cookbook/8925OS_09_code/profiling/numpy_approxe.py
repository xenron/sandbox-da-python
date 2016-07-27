import numpy
import cProfile
import pstats

def approx_e(n=40):
   # array of [1, 2, ... n-1]
   arr = numpy.arange(1, n) 

   # calculate the factorials and convert to floats
   arr = arr.cumprod().astype(float)

   # reciprocal 1/n
   arr = numpy.reciprocal(arr)

   print 1 + arr.sum() 

cProfile.runctx("approx_e()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()

