import scipy as sp
import scipy.stats as st
s = sp.randn(10)
n, min_max, mean, var, skew, kurt = st.describe(s)
print("Number of elements: {0:d}".format(n))
print("Minimum: {0:3.5f} Maximum: {1:2.5f}".format(min_max[0], min_max[1]))
print("Mean: {0:3.5f}".format(mean))
print("Variance: {0:3.5f}".format(var))
print("Skewness : {0:3.5f}".format(skew))
print("Kurtosis: {0:3.5f}".format(kurt))
