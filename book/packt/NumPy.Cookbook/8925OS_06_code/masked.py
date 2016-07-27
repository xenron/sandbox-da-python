import numpy
import scipy
import matplotlib.pyplot

lena = scipy.misc.lena()
random_mask = numpy.random.randint(0, 2, size=lena.shape)

matplotlib.pyplot.subplot(221)
matplotlib.pyplot.title("Original")
matplotlib.pyplot.imshow(lena)
matplotlib.pyplot.axis('off')

masked_array = numpy.ma.array(lena, mask=random_mask)
print masked_array

matplotlib.pyplot.subplot(222)
matplotlib.pyplot.title("Masked")
matplotlib.pyplot.imshow(masked_array)
matplotlib.pyplot.axis('off')

matplotlib.pyplot.subplot(223)
matplotlib.pyplot.title("Log")
matplotlib.pyplot.imshow(numpy.log(lena))
matplotlib.pyplot.axis('off')

matplotlib.pyplot.subplot(224)
matplotlib.pyplot.title("Log Masked")
matplotlib.pyplot.imshow(numpy.log(masked_array))
matplotlib.pyplot.axis('off')

matplotlib.pyplot.show()
