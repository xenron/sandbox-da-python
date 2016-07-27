import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def func(x, y):
	return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

points = np.random.rand(1000, 2)
values = func(points[:,0], points[:,1])
grid_z0 = griddata(points, values, (grid_x, grid_y), method=’nearest’)
grid_z1 = griddata(points, values, (grid_x, grid_y), method=’linear’)
grid_z2 = griddata(points, values, (grid_x, grid_y), method=’cubic’)

f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin=’lower’)
axarr[0, 0].plot(points[:,0], points[:,1], ’k.’, ms=1)
axarr[0, 0].set_title(’Original’)

axarr[0, 1].imshow(grid_z0.T, extent=(0,1,0,1), origin=’lower’)
axarr[0, 1].set_title(’Nearest’)

axarr[1, 0].imshow(grid_z1.T, extent=(0,1,0,1), origin=’lower’)
axarr[1, 0].set_title(’Linear’)

axarr[1, 1].imshow(grid_z2.T, extent=(0,1,0,1), origin=’lower’)
axarr[1, 1].set_title(’Cubic’)

plt.show()
