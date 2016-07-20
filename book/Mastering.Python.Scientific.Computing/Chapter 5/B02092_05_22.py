import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
tree = KDTree(points)
tree.query([0.1, 0.1])

x = np.linspace(-0.5, 2.5, 31)
y = np.linspace(-0.5, 2.5, 33)
xx, yy = np.meshgrid(x, y)
xy = np.c_[xx.ravel(), yy.ravel()]

plt.pcolor(x, y, tree.query(xy)[1].reshape(33, 31))
plt.plot(points[:,0], points[:,1], ’ko’)
plt.show()