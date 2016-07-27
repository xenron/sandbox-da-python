#!/usr/bin/env python

import numpy
import sys
import matplotlib.pyplot as pyplot

func = numpy.poly1d(numpy.array(sys.argv[1:]).astype(float))
x = numpy.linspace(-10, 10, 30)
y = func(x)
func1 = func.deriv(m=1)
y1 = func1(x)
func2 = func.deriv(m=2)
y2 = func2(x)

pyplot.subplot(311)
pyplot.plot(x, y, 'r-')
pyplot.title("Polynomial")
pyplot.subplot(312)
pyplot.plot(x, y1, 'b^')
pyplot.title("First Derivative")
pyplot.subplot(313)
pyplot.plot(x, y2, 'go')
pyplot.title("Second Derivative")
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()

