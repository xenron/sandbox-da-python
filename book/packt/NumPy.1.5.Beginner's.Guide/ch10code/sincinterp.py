#!/usr/bin/env python

import numpy
import scipy.interpolate
import matplotlib.pyplot

x = numpy.linspace(-18, 18, 36)
noise = 0.1 * numpy.random.random(len(x))
signal = numpy.sinc(x) + noise

interpreted = scipy.interpolate.interp1d(x, signal)
x2 = numpy.linspace(-18, 18, 180)
y = interpreted(x2)

cubic = scipy.interpolate.interp1d(x, signal, kind="cubic")
y2 = cubic(x2)

matplotlib.pyplot.plot(x, signal, 'o', label="data")
matplotlib.pyplot.plot(x2, y, '-', label="linear")
matplotlib.pyplot.plot(x2, y2, '-', lw=2, label="cubic")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

