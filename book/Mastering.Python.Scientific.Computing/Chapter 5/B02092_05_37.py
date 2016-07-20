import numpy as np
from scipy.stats import genpareto
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

c = 0.1
mean, var, skew, kurt = genpareto.stats(c, moments='mvsk')
x = np.linspace(genpareto.ppf(0.01, c),genpareto.ppf(0.99, c), 100)
ax.plot(x, genpareto.pdf(x, c),'r-', lw=5, alpha=0.6, label='genpareto pdf')
rv = genpareto(c)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
vals = genpareto.ppf([0.001, 0.5, 0.999], c)
np.allclose([0.001, 0.5, 0.999], genpareto.cdf(vals, c))
r = genpareto.rvs(c, size=1000)
ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()