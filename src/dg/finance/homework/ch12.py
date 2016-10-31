# -*- coding: utf-8 -*-

# 1. 假设S(0)=50，r=0.5%,u=0.01,d=-0.01,计算行权价为X=60，T=50时段以后行权的欧式看涨期权价格（基于二叉树模型）
# 2. 假设S(0)=100，r=0.5%, 波动率为0.25。计算行权价为X=95，一年后行权的美式看跌期权价格

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

###欧式期权###
#初始参数
S0 = 100.  #标的资产初始价格
r = 0.005   #无风险利率
sigma = 0.25   #标的资产波动率
T = 1.0   #到期日
I = 50000  #模拟数量

#二项分布模拟
def bin_sn(T, I, p = None):
    ''' Function to generate random numbers for simulation.
    
    Parameters
    ==========
    T : int
        周期数
    I : int
        模拟数量
    p : float
        风险中性概率

    '''
    sn = npr.binomial(T,p,size=I)
    return sn

#二叉树模型下的看涨期权估值   
def CRRF(K,u,d,T):
    ''' 
    基于二叉树模型使用蒙特卡洛方法模拟计算欧式看涨期权的价格
    
    Parameters
    ==========
    K : float
        行权价
    u : float
        股票上涨比率
    d : float
        股票下降比率
    
    Returns
    =======
    C0 : float
        对欧式看涨期权的估值
    '''
    print((r-d)/(u-d))
    sn = bin_sn(T, I, p=(r-d)/(u-d)) 
    #随机生成标的资产的到期价格
    ST = S0 *((1+u)**sn)*((1+d)**(T-sn))
    
    # 计算
    # 看涨期权
    hT = np.maximum(ST-K, 0)
    # 看跌期权
    # hT = np.maximum(K-ST, 0)
    
    # calculate MCS estimator
    C0 = np.exp(-r * T) * 1 / I * np.sum(hT)
    return C0    

CRRF(K=60,u=0.01,d=-0.01,T=T)    
CRRF(K=60,u=0.01,d=-0.01,T=50)   

##################################################################################
##################################################################################
##################################################################################

# 周期数
M = 365

#定义正态分布随机数生成函数
def gen_sn(M, I, anti_paths=True, mo_match=True):
    ''' Function to generate random numbers for simulation.
    
    Parameters
    ==========
    M : int
        周期数
    I : int
        模拟数量
    anti_paths: boolean
        是否使用对偶变量（若是，则只提取I的一半数目的随机数，另一半取其相反数获得）
    mo_math : boolean
        是否使用距匹配方法（若是，使用标准化方法校正生成的随机数）
    '''
    if anti_paths is True:
        sn = npr.standard_normal((M + 1, I / 2))
        sn = np.concatenate((sn, -sn), axis=1)
    else:
        sn = npr.standard_normal((M + 1, I))
    if mo_match is True:
        sn = (sn - sn.mean()) / sn.std()
    return sn

###美式期权###
def gbm_mcs_amer(K, option='call'):
    ''' Valuation of American option in Black-Scholes-Merton
    by Monte Carlo simulation by LSM algorithm
    
    Parameters
    ==========
    K : float
        行权价
    option : string
        期权类型 ('call', 'put')
    
    Returns
    =======
    C0 : float
        美式期权现值的估计
    '''
    dt = T / M
    df = np.exp(-r * dt)
    # 模拟价格路径
    S = np.zeros((M + 1, I))
    S[0] = S0
    sn = gen_sn(M, I)
    for t in range(1, M + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt 
                + sigma * np.sqrt(dt) * sn[t])
    # 回报计算
    if option == 'call':
        h = np.maximum(S - K, 0)
    else:
        h = np.maximum(K - S, 0)
    # LSM算法
    V = np.copy(h)
    for t in range(M - 1, 0, -1):
        reg = np.polyfit(S[t], V[t + 1] * df, 7)
        C = np.polyval(reg, S[t])
        V[t] = np.where(C > h[t], V[t + 1] * df, h[t])
    # MCS估计值
    C0 = df * 1 / I * np.sum(V[1])
    return C0
    
# 看跌期权价格
gbm_mcs_amer(95., option='put')





