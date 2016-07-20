import numpy as np
from scipy.stats import gengamma
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
a, c = 4.41623854294, 3.11930916792
mean, var, skew, kurt = gengamma.stats(a, c, moments='mvsk')
x = np.linspace(gengamma.ppf(0.01, a, c),gengamma.ppf(0.99, a, c), 100)
ax.plot(x, gengamma.pdf(x, a, c),'r-', lw=5, alpha=0.6, label='gengamma pdf')
plt.show()