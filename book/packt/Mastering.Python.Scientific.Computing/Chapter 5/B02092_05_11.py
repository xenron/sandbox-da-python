import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import special
from scipy import integrate

result = integrate.quad(lambda x: special.jv(4,x), 0, 20)
print result 
#the following line is calculating Gaussian Integral using quad function
print "Gaussian integral", np.sqrt(np.pi),quad(lambda x: np.exp(-x**2),-np.inf, np.inf)