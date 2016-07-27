#!/usr/bin/python

import numpy
from pylab import *

window = numpy.bartlett(42)
plot(window)
show()
