import numpy as np
from scipy.fftpack import fft, ifft
x = np.random.random_sample(5) #np.array([1.0, 2.5, 3.2, 4.0, 5.5])
y = fft(x)
print y
yinv = ifft(y)
print yinv