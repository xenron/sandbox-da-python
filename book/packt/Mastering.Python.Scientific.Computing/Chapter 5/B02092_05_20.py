import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
points = np.array([[0, 0], [1, 2], [1, 1], [1, 2]])
tri = Delaunay(points)
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.show()
plt.plot(points[:,0], points[:,1], ’o’)
plt.show()