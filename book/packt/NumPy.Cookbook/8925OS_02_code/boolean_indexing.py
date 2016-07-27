import scipy.misc
import matplotlib.pyplot
import numpy

# Load the Lena array
lena = scipy.misc.lena()

def get_indices(size):
   arr = numpy.arange(size)
   return arr % 4 == 0

# Plot Lena
lena1 = lena.copy() 
xindices = get_indices(lena.shape[0])
yindices = get_indices(lena.shape[1])
lena1[xindices, yindices] = 0
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.imshow(lena1)

lena2 = lena.copy() 
# Between quarter and 3 quarters of the max value
lena2[(lena > lena.max()/4) & (lena < 3 * lena.max()/4)] = 0
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.imshow(lena2)


matplotlib.pyplot.show()
