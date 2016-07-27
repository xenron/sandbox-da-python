#!/usr/bin/env python

import numpy
import sys
import matplotlib.pyplot as pyplot

func = numpy.poly1d(numpy.array(sys.argv[1:]).astype(float))
func1 = func.deriv(m=1)
x = numpy.linspace(-10, 10, 30)
y = func(x)
y1 = func1(x)

pyplot.plot(x, y, 'ro', x, y1, 'g--')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()

