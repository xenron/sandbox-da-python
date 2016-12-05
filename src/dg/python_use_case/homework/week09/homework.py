# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#读取数据
sales = pd.read_csv('d:/data/sales.csv')
sales.head()

#数据探索
sales.describe()

pd.value_counts(sales['ID'])
pd.value_counts(sales['Prod'])
pd.value_counts(sales['Insp'])
pd.value_counts(sales['Insp'])/len(sales)*100

print u'销售人员数量：' +str(len(set(sales['ID'])))
print u'销售产品数量：' +str(len(set(sales['Prod'])))

#缺失值统计
sum(sales['Quant'].isnull())
sum(sales['Val'].isnull())

s=pd.merge(pd.DataFrame(sales['Quant'].isnull()),
           pd.DataFrame(sales['Val'].isnull()),
           left_index=True,
           right_index=True)

len( s[s['Quant']][s['Val']])

naset = pd.merge(sales[s['Quant']],sales[s['Val']])

naprod = set(naset['Prod'])

#交易人员的交易数量分布
totS = pd.value_counts(sales['ID'])
totP = pd.value_counts(sales['Prod'])

totS.hist(bins=200)
totP.hist(bins=200)

#计算单位价格
sales['Uprice'] = sales['Val']/sales['Quant']
sales['Uprice'].describe()
sales['Uprice'].plot()

#产品价格分析
group = sales.groupby('Prod')
upp = group.median()['Uprice'].sort_values(ascending=False)
upp.head(5)
upp.tail(7)

top5 = upp.head(5).index
def a(x):
    return x in top5

pd.DataFrame(sales[sales['Prod'].apply(a)]['Uprice']).boxplot()


bott5 = upp.tail(7).index
def b(x):
    return x in bott5

pd.DataFrame(sales[sales['Prod'].apply(b)]['Uprice']).boxplot()

#销售人员销售记录分析
group = sales.groupby('ID')
upp = group.sum()['Val'].sort_values(ascending=False)
upp.head(5)
upp.tail(5)

top1 = upp.head(1).index
def a(x):
    return x in top1

(sales[sales['ID'].apply(a)]['Val'].sum()/sales['Val'].sum())*100

bott2000 = upp.tail(2000).index
def b(x):
    return x in bott2000

(sales[sales['ID'].apply(b)]['Val'].sum()/sales['Val'].sum())*100

#产品销售数量分析
group = sales.groupby('Prod')
upp = group.sum()['Quant'].sort_values(ascending=False)
upp.head(5)
upp.tail(7)

top100 = upp.head(100).index
def a(x):
    return x in top100

(sales[sales['Prod'].apply(a)]['Quant'].sum()/sales['Quant'].sum())*100

bott2000 = upp.tail(2000).index
def b(x):
    return x in bott2000

(sales[sales['Prod'].apply(b)]['Quant'].sum()/sales['Quant'].sum())*100


bott4000 = upp.tail(4000).index
def b(x):
    return x in bott4000

(sales[sales['Prod'].apply(b)]['Quant'].sum()/sales['Quant'].sum())*100

#箱线图离群值规则
#Q1-1.5*IQR ~ Q3+1.5*IQR
#IQR = Q3-Q1

Q1=sales['Uprice'].quantile(0.25)
Q3=sales['Uprice'].quantile(0.75)
IQR = Q3-Q1


def out(x):
    if x < Q1-1.5*IQR or x > Q3+1.5*IQR:
        return 1
    else:
        return 0
    
sales['out']=sales['Uprice'].apply(out)
    
outer = sales['out'].groupby(sales['Prod']).sum().sort_values(ascending=False)
outer.head(10)

sum(outer)

(0.1*sum(outer)/len(sales))*1000

###数据预处理###
#缺失值处理
from scipy.interpolate import lagrange 
def ployinterp_column(s, n, k=5):
    if n+1+k<len(s):
        lis=list(range(n-k, n)) + list(range(n+1,n+1+k ))
    else:
        lis=list(range(n-k, n)) + list(range(n+1, len(s)))
    y = s.iloc[lis]
    lis_2=pd.Series(lis)
    lis_2.index=y.index
    lis_2=list(lis_2[y.notnull()])
    y = y[y.notnull()] #剔除空值
    return lagrange(lis_2, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for x in naprod:
    data = sales[sales['Prod']==x]
    for i in ['Quant','Val']:
      m=0
      for j in data.index:        
        if (data[i].isnull())[j]: #如果为空即插值。
          sales[i][j] = ployinterp_column(s=data[i],n=m, k=5)
        m=m+1
        

sales['Quant'].loc[sales['Quant']<0 ]=sales['Quant'].median()
sales['Val'].loc[sales['Val']<0 ]=sales['Val'].median()
sales['Uprice'] = sales['Val']/sales['Quant']
sales.to_csv('d:/data/sales_2.csv')

sales = pd.read_csv('d:/data/sales_2.csv')

#少量交易产品
#检验两个数列是否同一分布
from scipy.stats import ks_2samp
beta=np.random.beta(7,5,1000)
norm=np.random.normal(0,1,1000)
ks_2samp(beta,norm)

###离群值判别###
prod=list(set(sales['Prod']))
data=sales[sales['Prod']==prod[2]]

import matplotlib.pyplot as plt  
f1 = plt.figure(1)  
plt.subplot(211)  
plt.scatter(sales['Quant'],sales['Val'])  

#参数初始化
k = 3 #聚类的类别
threshold = 2 #离散点阈值
iteration = 500 #聚类最大循环次数
data=data[['Quant','Val']]
data.dropna()
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类

#标准化数据及其类别
r = pd.concat([data_zs, pd.Series(model.labels_, index = data.index)], axis = 1)  #每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别'] #重命名表头

norm = []
for i in range(k): #逐一处理
  norm_tmp = r[['Quant','Val']][r[u'聚类类别'] == i]-model.cluster_centers_[i]
  norm_tmp = norm_tmp.apply(np.linalg.norm, axis = 1) #求出绝对距离
  norm.append(norm_tmp/norm_tmp.median()) #求相对距离并添加

norm = pd.concat(norm) #合并

plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
norm[norm <= threshold].plot(style = 'go') #正常点
discrete_points = norm[norm > threshold] #离群点
discrete_points.plot(style = 'ro')
for i in range(len(discrete_points)): #离群点做标记
  id = discrete_points.index[i]
  n = discrete_points.iloc[i]
  plt.annotate('(%s, %0.2f)'%(id, n), xy = (id, n), xytext = (id, n))
plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
plt.show()