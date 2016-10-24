# -*- coding: utf-8 -*-

import warnings
warnings.simplefilter('ignore')
import pymc3 as pm
import numpy as np
np.random.seed(1000)
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

#构造数据
x = np.linspace(0, 10, 500)
y = 4 + 2 * x + np.random.standard_normal(len(x)) * 2

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

fig = pm.traceplot(trace, lines={'alpha': 4, 'beta': 2, 'sigma': 2})
plt.figure(figsize=(8, 8))


plt.figure(figsize=(8, 4))
plt.scatter(x, y, c=y, marker='v')
plt.colorbar()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
for i in range(len(trace)):
    plt.plot(x, trace['alpha'][i] + trace['beta'][i] * x)
    
    
#真实数据
import warnings
warnings.simplefilter('ignore')
import zipline
import pytz
import datetime as dt  

data = zipline.data.load_from_yahoo(stocks=['GLD', 'GDX'], 
         end=dt.datetime(2014, 3, 15, 0, 0, 0, 0, pytz.utc)).dropna()
data.info()  

#折线图
data.plot(figsize=(8, 4))

#收益率
data.ix[-1] / data.ix[0] - 1

#相关系数
data.corr()

#data中的日期转换
data.index

import matplotlib as mpl
mpl_dates = mpl.dates.date2num(data.index.to_pydatetime())
mpl_dates

plt.figure(figsize=(8, 4))
plt.scatter(data['GDX'], data['GLD'], c=mpl_dates, marker='o')
plt.grid(True)
plt.xlabel('GDX')
plt.ylabel('GLD')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
             format=mpl.dates.DateFormatter('%d %b %y'))
             
#贝叶斯回归             
with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=0, sd=20)
    beta = pm.Normal('beta', mu=0, sd=20)
    sigma = pm.Uniform('sigma', lower=0, upper=50)
    
    y_est = alpha + beta * data['GDX'].values
    
    likelihood = pm.Normal('GLD', mu=y_est, sd=sigma,
                           observed=data['GLD'].values)
    
    start = pm.find_MAP()
    step = pm.NUTS(state=start)
    trace = pm.sample(100, step, start=start, progressbar=False)

fig = pm.traceplot(trace)
plt.figure(figsize=(8, 8))

plt.figure(figsize=(8, 4))
plt.scatter(data['GDX'], data['GLD'], c=mpl_dates, marker='o')
plt.grid(True)
plt.xlabel('GDX')
plt.ylabel('GLD')
for i in range(len(trace)):
    plt.plot(data['GDX'], trace['alpha'][i] + trace['beta'][i] * data['GDX'])
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
             format=mpl.dates.DateFormatter('%d %b %y'))

#假定回归参数随时间的推移随机游走
model_randomwalk = pm.Model()
with model_randomwalk:
    # std of random walk best sampled in log space
    sigma_alpha=pm.Exponential('sigma_alpha', 1. / .02,testval=.1)
    log_sigma_alpha=np.log(sigma_alpha)
    sigma_beta=pm.Exponential('sigma_beta',1. / .02, testval=.1)
    log_sigma_beta=np.log(sigma_beta)
#    sigma_alpha, log_sigma_alpha = model_randomwalk.TransformedVar('sigma_alpha', 
#                            pm.Exponential.dist(1. / .02, testval=.1), 
#                            pm.logtransform)
#    sigma_beta, log_sigma_beta = model_randomwalk.TransformedVar('sigma_beta', 
#                            pm.Exponential.dist(1. / .02, testval=.1),
#                            pm.logtransform)


from pymc3.distributions.timeseries import GaussianRandomWalk     

subsample_alpha = 50
subsample_beta = 50


with model_randomwalk:
    alpha = GaussianRandomWalk('alpha', sigma_alpha**(-2), 
                               shape=len(data) / subsample_alpha)
    beta = GaussianRandomWalk('beta', sigma_beta**-2, 
                              shape=len(data) / subsample_beta)
    
    # make coefficients have the same length as prices
    alpha_r = np.repeat(alpha, subsample_alpha)
    beta_r = np.repeat(beta, subsample_beta)

len(data.dropna().GDX.values)


with model_randomwalk:
    # define regression
    regression = alpha_r + beta_r * data.GDX.values[:1950]
    
    # assume prices are normally distributed,
    # the mean comes from the regression
    sd = pm.Uniform('sd', 0, 20)
    likelihood = pm.Normal('GLD', 
                           mu=regression, 
                           sd=sd, 
                           observed=data.GLD.values[:1950])
                           
import scipy.optimize as sco
with model_randomwalk:
    # first optimize random walk
    start = pm.find_MAP(vars=[alpha, beta], fmin=sco.fmin_l_bfgs_b)
    
    # sampling
    step = pm.NUTS(scaling=start)
    trace_rw = pm.sample(100, step, start=start, progressbar=False)                           

np.shape(trace_rw['alpha'])

part_dates = np.linspace(min(mpl_dates), max(mpl_dates), 39)

fig, ax1 = plt.subplots(figsize=(10, 5))
plt.plot(part_dates, np.mean(trace_rw['alpha'], axis=0),
         'b', lw=2.5, label='alpha')
for i in range(45, 55):
    plt.plot(part_dates, trace_rw['alpha'][i], 'b-.', lw=0.75)
plt.xlabel('date')
plt.ylabel('alpha')
plt.axis('tight')
plt.grid(True)
plt.legend(loc=2)
ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%d %b %y') )
ax2 = ax1.twinx()
plt.plot(part_dates, np.mean(trace_rw['beta'], axis=0),
         'r', lw=2.5, label='beta')
for i in range(45, 55):
    plt.plot(part_dates, trace_rw['beta'][i], 'r-.', lw=0.75)
plt.ylabel('beta')
plt.legend(loc=4)
fig.autofmt_xdate()


plt.figure(figsize=(10, 5))
plt.scatter(data['GDX'], data['GLD'], c=mpl_dates, marker='o')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
             format=mpl.dates.DateFormatter('%d %b %y'))
plt.grid(True)
plt.xlabel('GDX')
plt.ylabel('GLD')
x = np.linspace(min(data['GDX']), max(data['GDX'])) 
for i in range(39):
    alpha_rw = np.mean(trace_rw['alpha'].T[i])
    beta_rw = np.mean(trace_rw['beta'].T[i]) 
    plt.plot(x, alpha_rw + beta_rw * x, color=plt.cm.jet(256 * i / 39))

