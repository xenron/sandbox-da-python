import numpy as np
from scipy.integrate import quad, dblquad, fixed_quad

def integrand1 (t, x, n):
	return np.exp(-x*t) / t**n

n = 4
result = dblquad(lambda t, x: integrand1(t, x, n), 0, np.inf, lambda x: 0, lambda x: np.inf)


# the following code is performing Gaussian quadrature over a fixed interval
from scipy.integrate import fixed_quad, quadrature

def integrand(x, a, b):
	return a * x + b
a = 2
b = 1
fixed_result = fixed_quad(integrand, 0, 1, args=(a,b))
result  = quadrature(integrand, 0, 1, args=(a,b))