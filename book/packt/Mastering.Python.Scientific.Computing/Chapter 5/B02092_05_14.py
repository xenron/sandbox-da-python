import numpy as np
from scipy.integrate import simps
def func1(a,x):
	return a*x**2+2

def func2(b,x):
	return b*x**3+4

x = np.array([1, 2, 4, 5, 6])
y1 = func1(2,x)
Intgrl1 = simps(y1, x)

print(Intgrl1)

y2 = func2(3,x)
Intgrl2 = simps (y2,x)
print (Intgrl2)
