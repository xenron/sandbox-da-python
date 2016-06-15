#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

#Create a curve on the z axis.
x = np.linspace(0, 1, 100)
y = np.sin(x * -1 * np.pi) / 2 + 0.5

ax.plot(x, y, zs=0, zdir='z', label='Our random sin curve, only for z-axis')

'''Specify colors, and loop thru each and randomize the scatter dots, and add them to the chart data.'''
colors = ('r', 'g', 'k', 'b')
for c in colors:
    x = np.random.sample(42)
    y = np.random.sample(42)
    ax.scatter(x, y, 1, zdir='x', c=c)

#Apply the legend.
ax.legend()

#Add the X, Y, and Z axis.
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 1)

#Show the chart.
plt.show()