#!/usr/bin/env python

import scipy.misc
import numpy
import matplotlib.pyplot
import scipy.ndimage


image = scipy.misc.lena().astype(numpy.float32)

matplotlib.pyplot.subplot(221)
matplotlib.pyplot.title("Original Image") 
img = matplotlib.pyplot.imshow(image) 

matplotlib.pyplot.subplot(222) 
matplotlib.pyplot.title("Median Filter") 
filtered = scipy.ndimage.median_filter(image, size=(42,42))
matplotlib.pyplot.imshow(filtered) 

matplotlib.pyplot.subplot(223) 
matplotlib.pyplot.title("Rotated") 
rotated = scipy.ndimage.rotate(image, 90)
matplotlib.pyplot.imshow(rotated) 

matplotlib.pyplot.subplot(224) 
matplotlib.pyplot.title("Prewitt Filter") 
filtered = scipy.ndimage.prewitt(image)
matplotlib.pyplot.imshow(filtered) 
matplotlib.pyplot.show()
