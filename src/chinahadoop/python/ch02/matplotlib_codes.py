# coding:utf-8

'''
Created on Nov 20, 2016

@author: Bin Liang
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


# 创建figure
fig = plt.figure()

ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)

random_arr = np.random.randn(100)
plt.plot(random_arr)

#
x = np.linspace(-5, 15, 50)
ax2.plot(x, sp.stats.norm.pdf(x=x, loc=5, scale=2))
ax2.hist(sp.stats.norm.rvs(loc=5, scale=2, size=200), bins=50, normed=True, color='red', alpha=0.5)

# 绘制直方图
ax1.hist(np.random.randn(100), bins=10, color='b', alpha=0.3)

# 绘制散点图
x = np.arange(50)
y = x + 5 * np.random.rand(50)
ax3.scatter(x, y)

# 柱状图
ax5 = fig.add_subplot(2,3,5)
x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
width = 0.25
ax5.bar(x, y1, width, color='r')
ax5.bar(x+width, y2, width, color='g')
ax5.set_xticks(x+width)
ax5.set_xticklabels(['a', 'b', 'c', 'd', 'e'])
plt.show()

# 矩阵绘图
m = np.random.rand(10,10)
plt.imshow(m, interpolation='nearest', cmap=plt.cm.ocean)
plt.colorbar()
plt.show()

# plt.subplots()
fig, subplot_arr = plt.subplots(2,2)
subplot_arr[0,0].hist(np.random.randn(100), bins=10, color='b', alpha=0.3)
plt.show()
