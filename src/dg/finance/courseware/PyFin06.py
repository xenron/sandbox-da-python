# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import math
from scipy import stats
get_ipython().magic(u'matplotlib inline')


###收益率计算###
#简单收益率
def ret(pt,p0):
    print '简单收益率为'+str((pt-p0)/p0*100)+'%'
    return (pt-p0)/p0

ret(pt=393.01,p0=389.70)
ret(pt=390.66,p0=389.70)

#对数收益率
def log_ret(pt,p0):
    return math.log(pt/p0)
    
log_ret(pt=393.01,p0=389.70)
log_ret(pt=390.66,p0=389.70)   

#复合收益率
def k_ret(ret,k):
    print '到期收益率为'+str(((1+ret)**k-1)*100)+'%'
    return (1+ret)**k-1

k_ret(0.1,1)
k_ret(0.05,2)
k_ret(0.025,4)
k_ret(0.00863,12)
k_ret(0.1/52,52)
k_ret(0.1/365,365)

###随机变量与分布###
#####################
#二项分布
#####################
def test_binom_pmf():
    '''
    为离散分布
    二项分布的例子：抛掷10次硬币，恰好两次正面朝上的概率是多少？
    '''
    n = 10#独立实验次数
    p = 0.5#每次正面朝上概率
    k = np.arange(0,11)#0-10次正面朝上概率
    binomial = stats.binom.pmf(k,n,p)
    print binomial#概率和为1
    print sum(binomial)
    print binomial[2]

    plt.plot(k, binomial,'o-')
    plt.title('Binomial: n=%i , p=%.2f' % (n,p),fontsize=15)
    plt.xlabel('Number of successes')
    plt.ylabel('Probability of success',fontsize=15)
    plt.show()
test_binom_pmf()

def test_binom_rvs():
    '''
    为离散分布
    使用.rvs函数模拟一个二项随机变量，其中参数size指定你要进行模拟的次数。我让Python返回10000个参数为n和p的二项式随机变量
    进行10000次实验，每次抛10次硬币，统计有几次正面朝上，最后统计每次实验正面朝上的次数
    '''
    binom_sim = data = stats.binom.rvs(n=10,p=0.3,size=10000)
    print len(binom_sim)
    print "mean: %g" % np.mean(binom_sim)
    print "SD: %g" % np.std(binom_sim,ddof=1)

    plt.hist(binom_sim,bins=10,normed=True)
    plt.xlabel('x')
    plt.ylabel('density')
    plt.show()
test_binom_rvs()

#####################
#泊松分布
#####################
def test_poisson_pmf(rate=2):
    '''
    泊松分布的例子：已知某路口发生事故的比率是每天2次，那么在此处一天内发生4次事故的概率是多少？
    泊松分布的输出是一个数列，包含了发生0次、1次、2次，直到10次事故的概率。
    '''
    n = np.arange(0,10)
    y = stats.poisson.pmf(n,rate)
    print y
    plt.plot(n, y, 'o-')
    plt.title('Poisson: rate=%i' % (rate), fontsize=15)
    plt.xlabel('Number of accidents')
    plt.ylabel('Probability of number accidents', fontsize=15)
    plt.show()
test_poisson_pmf(2)
test_poisson_pmf(4)
test_poisson_pmf(10)

def test_poisson_rvs(mu=2, loc=0, size=1000):
    '''
    模拟1000个服从泊松分布的随机变量
    '''
    data = stats.poisson.rvs(mu, loc, size)
    print "mean: %g" % np.mean(data)
    print "SD: %g" % np.std(data, ddof=1)

    rate = 2
    n = np.arange(0,10)
    y = stats.poisson.rvs(n,rate)
    print y
    plt.plot(n, y, 'o-')
    plt.title('Poisson: rate=%i' % (rate), fontsize=15)
    plt.xlabel('Number of accidents')
    plt.ylabel('Probability of number accidents', fontsize=15)
    plt.show()
test_poisson_rvs()    

#####################
#正态分布
#####################
def test_norm_pmf():
    '''
    正态分布是一种连续分布，其函数可以在实线上的任何地方取值。
    正态分布由两个参数描述：分布的平均值μ和方差σ2 。
    '''
    mu = 0#mean
    sigma = 1#standard deviation
    x = np.arange(-5,5,0.1)
    y = stats.norm.pdf(x,0,1)
    print y
    plt.plot(x, y)
    plt.title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu,sigma))
    plt.xlabel('x')
    plt.ylabel('Probability density', fontsize=15)
    plt.show()
test_norm_pmf()

#####################
#beta分布
#####################
def test_beta_pmf():
    '''
    β分布是一个取值在 [0, 1] 之间的连续分布，它由两个形态参数α和β的取值所刻画。
    β分布的形状取决于α和β的值。贝叶斯分析中大量使用了β分布。
    '''
    a = 0.1#
    b = 0.8
    x = np.arange(0.01,1,0.01)
    y = stats.norm.pdf(x,a,b)
    print y
    plt.plot(x, y)
    plt.title('Beta: a=%.1f, b=%.1f' % (a,b))
    plt.xlabel('x')
    plt.ylabel('Probability density', fontsize=15)
    plt.show()

#####################
#指数分布（Exponential Distribution）
#####################
def test_exp():
    '''
    指数分布是一种连续概率分布，用于表示独立随机事件发生的时间间隔。
    比如旅客进入机场的时间间隔、打进客服中心电话的时间间隔、中文维基百科新条目出现的时间间隔等等。
    '''
    lambd = 0.5#
    x = np.arange(0,15,0.1)
    y =lambd * np.exp(-lambd *x)
    print y
    plt.plot(x, y)
    plt.title('Exponential: $\lambda$=%.2f' % (lambd))
    plt.xlabel('x')
    plt.ylabel('Probability density', fontsize=15)
    plt.show()

def test_expon_rvs():
    '''
    指数分布下模拟1000个随机变量。scale参数表示λ的倒数。函数np.std中，参数ddof等于标准偏差除以 $n-1$ 的值。
    '''
    data = stats.expon.rvs(scale=2, size=1000)
    print "mean: %g" % np.mean(data)
    print "SD: %g" % np.std(data, ddof=1)

    plt.hist(data, bins=20, normed=True)
    plt.xlim(0,15)
    plt.title('Simulating Exponential Random Variables')
    plt.show()
test_expon_rvs()

###随机数生成###
npr.rand(10)

npr.rand(5, 5)

a = 5.
b = 10.
npr.rand(10) * (b - a) + a

npr.rand(5, 5) * (b - a) + a

sample_size = 500
rn1 = npr.rand(sample_size, 3)
rn2 = npr.randint(0, 10, sample_size)
rn3 = npr.sample(size=sample_size)
a = [0, 25, 50, 75, 100]
rn4 = npr.choice(a, size=sample_size)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2,
                                             figsize=(7, 7))
ax1.hist(rn1, bins=25, stacked=True)
ax1.set_title('rand')
ax1.set_ylabel('frequency')
ax1.grid(True)
ax2.hist(rn2, bins=25)
ax2.set_title('randint')
ax2.grid(True)
ax3.hist(rn3, bins=25)
ax3.set_title('sample')
ax3.set_ylabel('frequency')
ax3.grid(True)
ax4.hist(rn4, bins=25)
ax4.set_title('choice')
ax4.grid(True)

sample_size = 500
rn1 = npr.standard_normal(sample_size)
rn2 = npr.normal(100, 20, sample_size)
rn3 = npr.chisquare(df=0.5, size=sample_size)
rn4 = npr.poisson(lam=1.0, size=sample_size)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
ax1.hist(rn1, bins=25)
ax1.set_title('standard normal')
ax1.set_ylabel('frequency')
ax1.grid(True)
ax2.hist(rn2, bins=25)
ax2.set_title('normal(100, 20)')
ax2.grid(True)
ax3.hist(rn3, bins=25)
ax3.set_title('chi square')
ax3.set_ylabel('frequency')
ax3.grid(True)
ax4.hist(rn4, bins=25)
ax4.set_title('Poisson')
ax4.grid(True)


####模拟####
# 随机变量

S0 = 100  # initial value
r = 0.05  # constant short rate
sigma = 0.25  # constant volatility
T = 2.0  # in years
I = 10000  # number of random draws
ST1 = S0 * np.exp((r - 0.5 * sigma ** 2) * T 
             + sigma * np.sqrt(T) * npr.standard_normal(I))

plt.hist(ST1, bins=50)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.grid(True)

ST2 = S0 * npr.lognormal((r - 0.5 * sigma ** 2) * T,
                        sigma * np.sqrt(T), size=I)

plt.hist(ST2, bins=50)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.grid(True)

import scipy.stats as scs

def print_statistics(a1, a2):
    ''' Prints selected statistics.
    
    Parameters
    ==========
    a1, a2 : ndarray objects
        results object from simulation
    '''
    sta1 = scs.describe(a1)
    sta2 = scs.describe(a2)
    print "%14s %14s %14s" %         ('statistic', 'data set 1', 'data set 2')
    print 45 * "-"
    print "%14s %14.3f %14.3f" % ('size', sta1[0], sta2[0])
    print "%14s %14.3f %14.3f" % ('min', sta1[1][0], sta2[1][0])
    print "%14s %14.3f %14.3f" % ('max', sta1[1][1], sta2[1][1])
    print "%14s %14.3f %14.3f" % ('mean', sta1[2], sta2[2])
    print "%14s %14.3f %14.3f" % ('std', np.sqrt(sta1[3]), np.sqrt(sta2[3]))
    print "%14s %14.3f %14.3f" % ('skew', sta1[4], sta2[4])
    print "%14s %14.3f %14.3f" % ('kurtosis', sta1[5], sta2[5])

print_statistics(ST1, ST2)

####随机过程###
#布朗运动
I = 10000
M = 50
dt = T / M
S = np.zeros((M + 1, I))
S[0] = S0
for t in range(1, M + 1):
    S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt 
            + sigma * np.sqrt(dt) * npr.standard_normal(I))
            
plt.hist(S[-1], bins=50)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.grid(True)

print_statistics(S[-1], ST2)

plt.plot(S[:, :10], lw=1.5)
plt.xlabel('time')
plt.ylabel('index level')
plt.grid(True)

####正态性检验####
#对数-正态价值
import numpy as np
np.random.seed(1000)
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

#模拟布朗运动
def gen_paths(S0, r, sigma, T, M, I):
    ''' Generate Monte Carlo paths for geometric Brownian motion.
    
    Parameters
    ==========
    S0 : float
        initial stock/index value
    r : float
        constant short rate
    sigma : float
        constant volatility
    T : float
        final time horizon
    M : int
        number of time steps/intervals
    I : int
        number of paths to be simulated
        
    Returns
    =======
    paths : ndarray, shape (M + 1, I)
        simulated paths given the parameters
    '''
    dt = float(T) / M
    paths = np.zeros((M + 1, I), np.float64)
    paths[0] = S0
    for t in range(1, M + 1):
        rand = np.random.standard_normal(I)
        rand = (rand - rand.mean()) / rand.std()
        paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt +
                                         sigma * np.sqrt(dt) * rand)
    return paths

S0 = 100.
r = 0.05
sigma = 0.2
T = 1.0
M = 50
I = 250000

paths = gen_paths(S0, r, sigma, T, M, I)

plt.plot(paths[:, :10])
plt.grid(True)
plt.xlabel('time steps')
plt.ylabel('index level')

#对数收益率计算
log_returns = np.log(paths[1:] / paths[0:-1]) 

paths[:, 0].round(4)

log_returns[:, 0].round(4)

#输出给定数据集的基本统计量
def print_statistics(array):
    ''' Prints selected statistics.
    
    Parameters
    ==========
    array: ndarray
        object to generate statistics on
    '''
    sta = scs.describe(array)
    print "%14s %15s" % ('statistic', 'value')
    print 30 * "-"
    print "%14s %15.5f" % ('size', sta[0])
    print "%14s %15.5f" % ('min', sta[1][0])
    print "%14s %15.5f" % ('max', sta[1][1])
    print "%14s %15.5f" % ('mean', sta[2])
    print "%14s %15.5f" % ('std', np.sqrt(sta[3]))
    print "%14s %15.5f" % ('skew', sta[4])
    print "%14s %15.5f" % ('kurtosis', sta[5])
    
print_statistics(log_returns.flatten())

plt.hist(log_returns.flatten(), bins=70, normed=True, label='frequency')
plt.grid(True)
plt.xlabel('log-return')
plt.ylabel('frequency')
x = np.linspace(plt.axis()[0], plt.axis()[1])
plt.plot(x, scs.norm.pdf(x, loc=r / M, scale=sigma / np.sqrt(M)),
         'r', lw=2.0, label='pdf')
plt.legend()

#正态性检验
sm.qqplot(log_returns.flatten()[::500], line='s')
plt.grid(True)
plt.xlabel('theoretical quantiles')
plt.ylabel('sample quantiles')

def normality_tests(arr):
    ''' Tests for normality distribution of given data set.
    
    Parameters
    ==========
    array: ndarray
        object to generate statistics on
    '''
    print "Skew of data set  %14.3f" % scs.skew(arr)
    print "Skew test p-value %14.3f" % scs.skewtest(arr)[1]
    print "Kurt of data set  %14.3f" % scs.kurtosis(arr)
    print "Kurt test p-value %14.3f" % scs.kurtosistest(arr)[1]
    print "Norm test p-value %14.3f" % scs.normaltest(arr)[1]
    
normality_tests(log_returns.flatten())

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))
ax1.hist(paths[-1], bins=30)
ax1.grid(True)
ax1.set_xlabel('index level')
ax1.set_ylabel('frequency')
ax1.set_title('regular data')
ax2.hist(np.log(paths[-1]), bins=30)
ax2.grid(True)
ax2.set_xlabel('log index level')
ax2.set_title('log data')

print_statistics(paths[-1])

print_statistics(np.log(paths[-1]))

normality_tests(np.log(paths[-1]))

log_data = np.log(paths[-1])
plt.hist(log_data, bins=70, normed=True, label='observed')
plt.grid(True)
plt.xlabel('index levels')
plt.ylabel('frequency')
x = np.linspace(plt.axis()[0], plt.axis()[1])
plt.plot(x, scs.norm.pdf(x, log_data.mean(), log_data.std()),
         'r', lw=2.0, label='pdf')
plt.legend()

sm.qqplot(log_data, line='s')
plt.grid(True)
plt.xlabel('theoretical quantiles')
plt.ylabel('sample quantiles')

##真实数据
import pandas as pd
import pandas_datareader.data as web


symbols = ['^GDAXI', '^GSPC', 'YHOO', 'MSFT']

data = pd.DataFrame()
for sym in symbols:
    data[sym] = web.DataReader(sym, data_source='yahoo',
                            start='1/1/2006')['Adj Close']
data = data.dropna()

data.info()

data.head()

(data / data.ix[0] * 100).plot(figsize=(8, 6), grid=True)

log_returns = np.log(data / data.shift(1))
log_returns.head()

log_returns.hist(bins=50, figsize=(9, 6))

for sym in symbols:
    print "\nResults for symbol %s" % sym
    print 30 * "-"
    log_data = np.array(log_returns[sym].dropna())
    print_statistics(log_data)
    
sm.qqplot(log_returns['^GSPC'].dropna(), line='s')
plt.grid(True)
plt.xlabel('theoretical quantiles')
plt.ylabel('sample quantiles')

sm.qqplot(log_returns['MSFT'].dropna(), line='s')
plt.grid(True)
plt.xlabel('theoretical quantiles')
plt.ylabel('sample quantiles')

for sym in symbols:
    print "\nResults for symbol %s" % sym
    print 32 * "-"
    log_data = np.array(log_returns[sym].dropna())
    normality_tests(log_data)
