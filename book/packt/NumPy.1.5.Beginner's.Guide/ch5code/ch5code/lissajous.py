#!/usr/bin/python

import numpy
from pylab import *
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
t = numpy.linspace(-numpy.pi, numpy.pi, 201)
x = numpy.sin(a * t + numpy.pi/2)
y = numpy.sin(b * t)
plot(x, y)
show()

