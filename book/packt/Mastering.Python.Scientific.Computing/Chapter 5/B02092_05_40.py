import numpy as np
from scipy import signal
from scipy import misc
lena = misc.lena()
noisy_lena = np.copy(lena).astype(np.float)
noisy_lena += lena.std()*0.5*np.random.standard_normal(lena.shape)

f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(noisy_lena, cmap=plt.cm.gray)
axarr[0, 0].axis('off')
axarr[0, 0].set_title('Noissy Lena Image')

blurred_lena = ndimage.gaussian_filter(noisy_lena, sigma=3)
axarr[0, 1].imshow(blurred_lena, cmap=plt.cm.gray)
axarr[0, 1].axis('off')
axarr[0, 1].set_title('Blurred Lena')

median_lena = ndimage.median_filter(blurred_lena, size=5)
axarr[1, 0].imshow(median_lena, cmap=plt.cm.gray)
axarr[1, 0].axis('off')
axarr[1, 0].set_title('Median Filter Lena')

wiener_lena = signal.wiener(blurred_lena, (5,5))
axarr[1, 1].imshow(wiener_lena, cmap=plt.cm.gray)
axarr[1, 1].axis('off')
axarr[1, 1].set_title('Wiener Filter Lena')

plt.show()
