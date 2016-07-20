import numpy as np
from scipy.optimize import minimize
def rosenbrock(x):
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])

def rosen_derivative(x):
	xm = x[1:-1]
	xm_m1 = x[:-2]
	xm_p1 = x[2:]
	derivative = np.zeros_like(x)
	derivative[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
	derivative[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
	derivative[-1] = 200*(x[-1]-x[-2]**2)
	return derivative

res = minimize(rosenbrock, x0, method=’BFGS’, jac=rosen_derivative, options={’disp’: True})