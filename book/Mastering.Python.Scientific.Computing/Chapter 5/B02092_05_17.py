import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
img = misc.lena()

splineresult = signal.cspline2d(img, 2.0)
laplacian = np.array([[-1,0,1], [-2,0,2], [-1,0,1]], dtype=np.float32)
derivative = signal.convolve2d(splineresult,laplacian,mode=’same’,boundary=’symm’)
plt.figure()
plt.imshow(derivative)
plt.title(’Image filtered by spline edge filter’)
plt.show()