import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
	return x**2 + 10*np.sin(x)

x = np.arange(-10,10,0.1)
plt.plot(x, f(x))
plt.show()

optimize.fmin_bfgs(f, 0)

grid = (-10, 10, 0.1)
optimize.brute(f, (grid,))
optimize.brent(f)
optimize.fminbound(f, 0, 10)