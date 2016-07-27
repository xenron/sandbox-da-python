#!/usr/bin/python

import numpy
from pylab import *

x =  numpy.linspace(0, 2 * numpy.pi, 30)
wave = numpy.cos(x)
transformed = numpy.fft.fft(wave)
print numpy.all(numpy.abs(numpy.fft.ifft(transformed) - wave) < 10 ** -9)

plot(transformed)
show()
