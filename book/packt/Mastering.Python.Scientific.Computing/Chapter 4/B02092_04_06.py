import numpy as np
from scipy.optimize import minimize
def rosen(x):
     return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
x0 = np.array([1, 0.7, 0.8, 2.9, 1.1])
res = minimize(rosen, x0, method='nelder-mead',
                options={'xtol': 1e-8, 'disp': True})
print(res.x)