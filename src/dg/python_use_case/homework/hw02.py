# -*- coding: utf-8 -*-

# 利用2015xxxx文件夹中的原始汇总数据，构建出站点的上下班时间段进站日均人数、上下班时间段出站日均人数、非上下班时间段进站日均人数、非上下班时间段出站日均人数 四个变量。
# 对这四个变量进行聚类分析

#读取数据
import pandas as pd
data=pd.read_excel(u'd:/tmp/hw02-data2.xlsx',index_col=u'index')
data.head()

#数据预处理
data_in = pd.DataFrame(data[data.type=='in'][['rush','no-rush','station']])
data_in.columns = ['rush-in','no-rush-in','station']
data_out = pd.DataFrame(data[data.type=='out'][['rush','no-rush','station']])
data_out.columns = ['rush-out','no-rush-out','station']
data = data_in.merge(data_out)
data.index = data['station']
data = data[['rush-in','no-rush-in','rush-out','no-rush-out']]

data = (data - data.min())/(data.max() - data.min()) #离差标准化
data=data.fillna(0)  #处理na值

####模型构建####
##系谱图绘制
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
#这里使用scipy的层次聚类函数

Z = linkage(data, method = 'ward', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()


##层次聚类算法
#参数初始化
k = 3 #聚类数

#模型构建
from sklearn.cluster import AgglomerativeClustering #导入sklearn的层次聚类函数
model = AgglomerativeClustering(n_clusters = k, linkage = 'ward')
model.fit(data) #训练模型


#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别'] #重命名表头

import matplotlib.pyplot as plt

style = ['ro-', 'go-', 'bo-']
xlabels = [u'上下班时间段进站日均人数', u'上下班时间段出站日均人数', u'非上下班时间段进站日均人数', u'非上下班时间段出站日均人数']
pic_output = 'd:/data/example02/type_' #聚类图文件名前缀

for i in range(k): #逐一作图，作出不同样式
  plt.figure()
  tmp = r[r[u'聚类类别'] == i].iloc[:,:4] #提取每一类
  for j in range(len(tmp)):
    plt.plot(range(1, 5), tmp.iloc[j], style[i])
  
  plt.xticks(range(1, 5), xlabels, rotation = 20,fontproperties='SimHei') #坐标标签
  plt.title(u'商圈类别%s' %(i+1),fontproperties='SimHei') #我们计数习惯从1开始
  plt.subplots_adjust(bottom=0.15) #调整底部
  plt.savefig(u'%s%s.png' %(pic_output, i+1)) #保存图片

