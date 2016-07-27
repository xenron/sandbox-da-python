import scipy.misc
import matplotlib.pyplot

lena = scipy.misc.lena()
acopy = lena.copy()
aview = lena.view()

# Plot the Lena array
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.imshow(lena)

#Plot the copy
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.imshow(acopy)

#Plot the view
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.imshow(aview)

# Plot the view after changes
aview.flat = 0
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.imshow(aview)

matplotlib.pyplot.show()

