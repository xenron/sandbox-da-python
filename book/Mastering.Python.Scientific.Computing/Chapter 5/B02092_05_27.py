import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
x = np.linspace(0, 20, 10)
y = np.cos(-x**3/5.0)

f = interp1d(x, y)
xnew = np.linspace(0, 20, 25)

plt.plot(x,y,’o’,xnew,f(xnew),’-’)
plt.legend([’data’, ’linear’], loc=’best’)
plt.show()