import scipy.misc
import matplotlib.pyplot

# Load the Lena array
lena = scipy.misc.lena()

# Plot the Lena array
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.imshow(lena)

#Plot the flipped array
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.imshow(lena[:,::-1])

#Plot a slice array
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.imshow(lena[:lena.shape[0]/2,:lena.shape[1]/2])

# Apply a mask
mask = lena % 2 == 0
masked_lena = lena.copy()
masked_lena[mask] = 0
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.imshow(masked_lena)

matplotlib.pyplot.show()
