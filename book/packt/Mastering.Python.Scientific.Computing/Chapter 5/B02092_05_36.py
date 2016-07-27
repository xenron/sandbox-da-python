import numpy as np
from scipy.stats import geom
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
p = 0.5
mean, var, skew, kurt = geom.stats(p, moments='mvsk')
x = np.arange(geom.ppf(0.01, p),geom.ppf(0.99, p))
ax.plot(x, geom.pmf(x, p), 'bo', ms=8, label='geom pmf')
ax.vlines(x, 0, geom.pmf(x, p), colors='b', lw=5, alpha=0.5)
plt.show()