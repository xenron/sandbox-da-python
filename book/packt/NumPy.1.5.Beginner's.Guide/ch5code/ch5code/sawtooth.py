#!/usr/bin/python

import numpy
from pylab import *
import sys

t = numpy.linspace(-numpy.pi, numpy.pi, 201)
k = numpy.arange(1, float(sys.argv[1]))
f = numpy.zeros_like(t)

for i in range(len(t)):
   f[i] = numpy.sum(numpy.sin(2 * numpy.pi * k * t[i])/k)

f = (-2 / numpy.pi) * f
plot(t, f, lw=1.0)
plot(t, numpy.abs(f), lw=2.0)
show()
