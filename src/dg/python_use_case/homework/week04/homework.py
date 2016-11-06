# -*- coding: utf-8 -*-

###数据准备###
import pandas as pd

#读入数据
data=pd.read_excel(u'D:/tmp/github/my/sandbox-da-python/src/dg/python_use_case/homework/week04/data.xls',index_col=u'MEMBER_NO')


###数据探索###
import matplotlib.pyplot as plt
data.describe()

pd.value_counts(data['Gender'])
pd.value_counts(data['Tariff'])
pd.value_counts(data['Handset'])

for col in data.columns:
    if not col in [u'Gender',u'Tariff',u'Handset']:
        fig = plt.figure()
        ax=fig.add_subplot(1,1,1)
        data[col].hist(bins=20)
        ax.set_title(col)
        fig.show()
        
###模型建立###
#数据整理
cols= data.columns.diff([u'Age',u'Gender',u'Tariff',u'Handset'])
cols
data_zs = 1.0*(data[cols] - data[cols].mean())/data[cols].std() #数据标准化
#dumies=pd.get_dummies(data[[u'Tariff',u'Handset']]) #获取虚拟变量
##合并数据
#data_zs = data_zs.merge(dumies,left_index=True,right_index=True)

#聚类数目
from scipy.cluster.hierarchy import linkage,dendrogram

Z = linkage(data_zs, method = 'ward', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()

#参数初始化
k = 4 #聚类的类别
iteration = 500 #聚类最大循环次数

#构建k-means模型
from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类

#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心

r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data_zs.columns) + [u'class'] #重命名表头
print(r)

#类中心比较
r[cols].plot(figsize=(10,10))
plt.show()


#详细输出原始数据及其类别
res = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
res.columns = list(data.columns) + [u'class'] #重命名表头
res.to_excel('d:/data/example04/result.xls') #保存结果

pd.crosstab(res['Tariff'],res['class'])
pd.crosstab(res['Handset'],res['class'])
pd.crosstab(res['Gender'],res['class'])

res[[u'Age',u'class']].hist(by='class')
res[u'Age'].groupby(res['class']).mean()


def density_plot(data): #自定义作图函数
  import matplotlib.pyplot as plt
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False,figsize=(10,15) )
  [p[i].set_ylabel(u'密度',fontproperties='SimHei') for i in range(k)]
  plt.legend()
  return plt

pic_output = 'd:/data/example04/pd_' #概率密度图文件名前缀
for i in range(k):
  density_plot(data[res[u'class']==i]).savefig(u'%s%s.png' %(pic_output, i))       

