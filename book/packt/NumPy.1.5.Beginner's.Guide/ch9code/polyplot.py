#!/usr/bin/env python

import numpy
import sys
import matplotlib.pyplot as pyplot

func = numpy.poly1d(numpy.array(sys.argv[1:]).astype(float))
x = numpy.linspace(-10, 10, 30)
y = func(x)

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y(x)')
pyplot.show()

