import numpy
import matplotlib.pyplot
from random import choice
import sys
import scipy
import scipy.ndimage

# Initialization
NFIGURES = int(sys.argv[1])
k = numpy.random.random_integers(1, 5, NFIGURES)
a = numpy.random.random_integers(1, 5, NFIGURES)

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

lena = scipy.misc.lena()
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.imshow(lena)
matplotlib.pyplot.axis('off')

# Blur Lena
matplotlib.pyplot.subplot(212)
blurred = scipy.ndimage.gaussian_filter(lena, sigma=4)

matplotlib.pyplot.imshow(blurred)
matplotlib.pyplot.axis('off')

# Plot in polar coordinates
theta = numpy.linspace(0, k[0] * numpy.pi, 200)
matplotlib.pyplot.polar(theta, numpy.sqrt(theta), choice(colors))

for i in xrange(1, NFIGURES):
   theta = numpy.linspace(0, k[i] * numpy.pi, 200)
   matplotlib.pyplot.polar(theta, a[i] * numpy.cos(k[i] * theta), choice(colors))

matplotlib.pyplot.axis('off')

matplotlib.pyplot.show()
