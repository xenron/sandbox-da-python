import matplotlib.pyplot as plt
from numpy import *
var = random.randn(5300)
plt.hist(var, 530)
plt.title(r'Normal distribution ($\mu=0, \sigma=1$)')
plt.show()