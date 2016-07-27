import numpy_api_demo as npd
import numpy as np
import pylab

#x = np.arange(0, 2 * np.pi, 0.1)
x = np.arange(0, 200, 1.0)
y = npd.np_square(x)
pylab.plot(x, y)
pylab.show()
print y
