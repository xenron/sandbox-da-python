import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
randpoints = np.random.rand(25, 2) # 30 random points in 2-D
hull = ConvexHull(randpoints)
plt.plot(randpoints[:,0], randpoints[:,1], ’o’)
for simplex in hull.simplices:
	plt.plot(randpoints[simplex,0], randpoints[simplex,1], ’k-’)

plt.show()