#!/usr/bin/python

import numpy
import matplotlib.pyplot

N=10000

normal_values = numpy.random.normal(size=N)
dummy, bins, dummy = matplotlib.pyplot.hist(normal_values, numpy.sqrt(N), normed=True, lw=1)
sigma = 1
mu = 0
matplotlib.pyplot.plot(bins, 1/(sigma * numpy.sqrt(2 * numpy.pi)) * numpy.exp( - (bins - mu)**2 / (2 * sigma**2) ),lw=2)
matplotlib.pyplot.show()


