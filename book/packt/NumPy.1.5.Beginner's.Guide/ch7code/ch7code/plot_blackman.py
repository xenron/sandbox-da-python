#!/usr/bin/python

import numpy
from pylab import *
import sys


closes=numpy.loadtxt('AAPL.csv', delimiter=',', usecols=(6,), converters={1:datestr2num}, unpack=True)
N = int(sys.argv[1])
window = numpy.blackman(N)
smoothed = numpy.convolve(window/window.sum(), closes, mode='same')
plot(smoothed[N:-N], lw=2, label="smoothed")
plot(closes[N:-N], label="closes")
legend(loc='best')
show()
