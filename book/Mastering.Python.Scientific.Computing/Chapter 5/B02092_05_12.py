import numpy as np
from scipy.integrate import quad

def integrand(x, a, b, c):
	return a*x*x+b*x+c

a = 3
b = 4 
c = 1
result = quad(integrand, 0,np.inf,  args=(a,b,c))
print result
