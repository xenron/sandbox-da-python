#!/usr/bin/python

import numpy
from pylab import *

x = numpy.linspace(0, 4, 100)
xx = numpy.outer(x, x)
vals = numpy.sinc(xx)

imshow(vals)
show()
