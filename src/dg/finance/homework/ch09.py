# -*- coding: utf-8 -*-

# 对数据集 ex09 做贝叶斯回归
import warnings
warnings.simplefilter('ignore')
import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


inputfile = 'd:/tmp/ex09.xlsx'
# 导入数据
data = pd.read_excel(inputfile)
# 构造数据，gas 和 crude oil，
x = data['gas']
y = data['crude oil']

#最小二乘回归
reg = np.polyfit(x, y, 1)

plt.figure(figsize=(8, 4))
plt.scatter(x, y, c=y, marker='v')
plt.plot(x, reg[1] + reg[0] * x, lw=2.0)
plt.colorbar()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

#估计参数
reg

#贝叶斯回归
with pm.Model() as model: 
    # 定义参数的先验概率
    alpha = pm.Normal('alpha', mu=0, sd=20)
    beta = pm.Normal('beta', mu=0, sd=20)
    sigma = pm.Uniform('sigma', lower=0, upper=10)
    # 定义线性回归方差
    y_est = alpha + beta * x
    # 定义极大似然度
    likelihood = pm.Normal('y', mu=y_est, sd=sigma, observed=y)
    # 寻找初始值
    start = pm.find_MAP()
    # 计算步长
    step = pm.NUTS(state=start)
    # 采样。样本容量为100
    trace = pm.sample(100, step, start=start, progressbar=False)
 
#观测来自第一个样本的估算   
trace[0]