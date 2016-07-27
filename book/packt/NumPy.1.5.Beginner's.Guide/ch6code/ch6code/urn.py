#!/usr/bin/python

import numpy
from pylab import *

points = numpy.zeros(100)
outcomes = numpy.random.hypergeometric(25, 1, 3, size=len(points))

for i in range(len(points)):
   if outcomes[i] == 3:
      points[i] = points[i - 1] + 1
   elif outcomes[i] == 2:
      points[i] = points[i - 1] - 6
   else:
      print outcomes[i]

plot(numpy.arange(len(points)), points)
show()
