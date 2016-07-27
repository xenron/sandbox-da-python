#!/usr/bin/python

import numpy
from pylab import *
import sys

t = numpy.linspace(-numpy.pi, numpy.pi, 201)
k = numpy.arange(1, float(sys.argv[1]))
k = 2 * k - 1
f = numpy.zeros_like(t)

for i in range(len(t)):
   f[i] = numpy.sum(numpy.sin(k * t[i])/k)

f = (4 / numpy.pi) * f
plot(t, f)
show()
