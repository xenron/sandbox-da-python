#!/usr/bin/python

import numpy
import matplotlib.pyplot

N=10000
lognormal_values = numpy.random.lognormal(size=N)
dummy, bins, dummy = matplotlib.pyplot.hist(lognormal_values, numpy.sqrt(N), normed=True, lw=1)
sigma = 1
mu = 0
x = numpy.linspace(min(bins), max(bins), len(bins))
pdf = numpy.exp(-(numpy.log(x) - mu)**2 / (2 * sigma**2))/ (x * sigma * numpy.sqrt(2 * numpy.pi))
matplotlib.pyplot.plot(x, pdf,lw=3)
matplotlib.pyplot.show()

