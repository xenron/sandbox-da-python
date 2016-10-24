# -*- coding: utf-8 -*-

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

###成本距离模型###
#读取数据
file_path=u'd:/data/example03/data.xlsx'
data=pd.read_excel(file_path,header=0,index_col=0)

#数据预分析
data.describe() #基本统计量
data.skew() #偏度
data.kurt() #超额峰度,大于0表示比正态分布陡峭，小于0表示比正态分布平缓
data.corr() #相关矩阵

data.iloc[:,:10].hist()


#数据预处理——主成分提取
pca = PCA()
pca.fit(data)
pca.explained_variance_ratio_

pca2=PCA(n_components=2)
reduce_X = pca2.fit_transform(data)
reduce_X

##系谱图绘制
#sdata= (data - data.mean())/data.std() #标准化
#sdata=sdata.fillna(0)  #处理na值
#sdata.to_excel('d:/data/example03/standata.xls',index=True) #保存结果

Z = linkage(reduce_X, method = 'ward', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()

#聚类分析
pd.DataFrame(reduce_X).plot(kind='scatter',x=0,y=1)
K = range(1, 6)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(reduce_X)
    meandistortions.append(sum(np.min(cdist(reduce_X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / reduce_X.shape[0])
fig = plt.figure()   
plt.plot(K, meandistortions, 'bx-')
plt.xlabel('k')
plt.ylabel('The average degree of distortion')
plt.title('Best k')

#模型构建
model = KMeans(n_clusters = 4)
model.fit(reduce_X)

#模型分析 
print(model.labels_)
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(pd.DataFrame(reduce_X).columns) + [u'类别数目'] #重命名表头
print(r)


###成本预测模型###
#数据读取
inputfile = u'D:/data/example03/data1.csv' #输入的数据文件
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
model.fit(data.iloc[:,0:13],data['y'])
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

data.index = range(1994, 2014)

data.loc[2014] = None
data.loc[2015] = None
l = ['x2', 'x3', 'x5', 'x8','x10','x12']
for i in l:
  f = GM11(data[i][range(1994, 2014)].as_matrix())[0]
  data[i][2014] = f(len(data)-1) #2014年预测结果
  data[i][2015] = f(len(data)) #2015年预测结果
  data[i] = data[i].round(2) #保留两位小数

outputfile=u'D:/data/example03/data1_GM11.xls'
data[l+['y']].to_excel(outputfile) #结果输出

#神经网络预测模型
inputfile = 'D:/data/example03/data1_GM11.xls'
outputfile = 'D:/data/example03/revenue.xls' #神经网络预测后保存的结果
modelfile = 'D:/data/example03/1-net.model' #模型保存路径
data = pd.read_excel(inputfile) #读取数据
feature = ['x2', 'x3', 'x5', 'x8','x10','x12'] #特征所在列

data_train = data.loc[range(1994,2014)].copy() #取2014年前的数据建模
data_mean = data_train.mean()
data_std = data_train.std()
data_train = (data_train - data_mean)/data_std #数据标准化
x_train = data_train[feature].as_matrix() #特征数据
y_train = data_train['y'].as_matrix() #标签数据

from keras.models import Sequential
from keras.layers.core import Dense, Activation

model = Sequential() #建立模型
model.add(Dense(input_dim=6, output_dim=12))
model.add(Activation('relu')) #用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(input_dim=12, output_dim=1))
model.compile(loss='mean_squared_error', optimizer='adam') #编译模型
model.fit(x_train, y_train, nb_epoch = 10000, batch_size = 16) #训练模型，学习一万次
model.save_weights(modelfile) #保存模型参数

#预测，并还原结果。
x = ((data[feature] - data_mean[feature])/data_std[feature]).as_matrix()
data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
data.to_excel(outputfile)

import matplotlib.pyplot as plt #画出预测结果图
p = data[['y','y_pred']].plot(subplots = True, style=['b-o','r-*'])
plt.show()
