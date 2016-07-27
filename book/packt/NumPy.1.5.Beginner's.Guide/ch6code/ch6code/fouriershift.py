#!/usr/bin/python

import numpy
from pylab import *

x =  numpy.linspace(0, 2 * numpy.pi, 30)
wave = numpy.cos(x)
transformed = numpy.fft.fft(wave)
shifted = numpy.fft.fftshift(transformed)
print numpy.all(numpy.abs(numpy.fft.ifftshift(shifted) - transformed) < 10 ** -9)


plot(transformed, lw=2)
plot(shifted, lw=3)
show()
