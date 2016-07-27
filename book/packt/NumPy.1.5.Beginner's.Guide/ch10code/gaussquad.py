#!/usr/bin/env python

import scipy.integrate
import numpy

print "Gaussian integral", numpy.sqrt(numpy.pi),scipy.integrate.quad(lambda x: numpy.exp(-x**2), -numpy.inf, numpy.inf)
