# -*- coding: utf-8 -*-

# 对data2.csv进行变量筛选，并构建预测模型

#加载所需的库
import numpy as np
import pandas as pd
from datetime import datetime 
from sklearn.decomposition import PCA,FactorAnalysis
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering,KMeans
from scipy import ndimage
from sklearn import manifold, datasets
from scipy.spatial.distance import cdist
from scipy.cluster.hierarchy import linkage,dendrogram

###成本预测模型###
#数据读取
inputfile = u'D:/data/data2.csv' #输入的数据文件
data = pd.read_csv(inputfile) #读取数据

#数据描述分析
r = [data.min(), data.max(), data.mean(), data.std()] #依次计算最小值、最大值、均值、标准差
r = pd.DataFrame(r, index = ['Min', 'Max', 'Mean', 'STD']).T  
np.round(r, 2) #保留两位小数

#相关分析
np.round(data.corr(method = 'pearson'), 2)

##模型构建
#Lasso变量选择
from sklearn.linear_model import LassoLars
model = LassoLars(alpha=0.1)
model.fit(data.iloc[:,0:6],data['y'])
np.round(pd.DataFrame(model.coef_),4) #各个特征的系数

#灰色预测模型
def GM11(x0): #自定义灰色预测函数
  import numpy as np
  x1 = x0.cumsum() #1-AGO序列
  z1 = (x1[:len(x1)-1] + x1[1:])/2.0 #紧邻均值（MEAN）生成序列
  z1 = z1.reshape((len(z1),1))
  B = np.append(-z1, np.ones_like(z1), axis = 1)
  Yn = x0[1:].reshape((len(x0)-1, 1))
  [[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Yn) #计算参数
  f = lambda k: (x0[0]-b/a)*np.exp(-a*(k-1))-(x0[0]-b/a)*np.exp(-a*(k-2)) #还原值
  delta = np.abs(x0 - np.array([f(i) for i in range(1,len(x0)+1)]))
  C = delta.std()/x0.std()
  P = 1.0*(np.abs(delta - delta.mean()) < 0.6745*x0.std()).sum()/len(x0)
  return f, a, b, x0[0], C, P #返回灰色预测函数、a、b、首项、方差比、小残差概率

data.index = range(1994, 2009)

data.loc[2009] = None
data.loc[2010] = None
l = ['x2', 'x3', 'x4','x6']
for i in l:
  f = GM11(data[i][range(1994, 2009)].as_matrix())[0]
  data[i][2009] = f(len(data)-1) #2014年预测结果
  data[i][2010] = f(len(data)) #2015年预测结果
  data[i] = data[i].round(2) #保留两位小数

outputfile=u'D:/tmp/data2_GM11.xls'
data[l+['y']].to_excel(outputfile) #结果输出
