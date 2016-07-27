#!/usr/bin/python

import numpy
from pylab import *

x = numpy.linspace(0, 4, 100)
vals = numpy.sinc(x)

plot(x, vals)
show()
