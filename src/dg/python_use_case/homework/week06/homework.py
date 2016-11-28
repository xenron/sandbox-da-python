# -*- coding: utf-8 -*-
###数据抽取###
#加载包
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

#连接数据库
engine = create_engine('mysql+pymysql://root:123456@192.168.101.81:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)
data_list = [ i for i in sql]
df = pd.concat(data_list)
df.columns
df.to_csv('d:/tmp/week06_data', encoding='utf-8', index=False)

all_data = pd.read_csv('d:/tmp/week06_data', encoding='utf-8')
all_data[['realIP', 'fullURL']]
all_data['fullURLId'].value_counts()
all_data.columns


####################################################################################################

###探索分析###
#网页类型分析
counts = [ i['fullURLId'].value_counts() for i in sql] #逐块统计
counts = pd.concat(counts).groupby(level=0).sum() #合并统计结果，把相同的统计项合并（即按index分组并求和）
counts = counts.reset_index() #重新设置index，将原来的index作为counts的一列。
counts.columns = ['index', 'num'] #重新设置列名，主要是第二列，默认为0
counts['type'] = counts['index'].str.extract('(\d{3})') #提取前三个数字作为类别id
counts_ = counts[['type', 'num']].groupby('type').sum()#按类别合并
counts_['ratio']=counts_/counts_.sum() #增加比例列
counts_.sort('num', ascending = False) #按类型编码顺序排序

#统计101类别的情况
counts_101=counts[counts['type']=='101'][['index', 'num']]
counts_101['ratio']=counts_101['num']/counts_101['num'].sum()
counts_101.sort('num', ascending = False)

#统计其他类别的情况
def counts_type(type):
    counts_type=counts[counts['type']==type][['index', 'num']]
    counts_type['ratio']=counts_type['num']/counts_type['num'].sum()
    return counts_type.sort('num', ascending = False)

counts_type('102')   

counts_type('103')  
  
#统计107类别的情况
def count107(i): #自定义统计函数
  j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy() #找出类别包含107的网址
  j['type'] = None #添加空列
  j['type'][j['fullURL'].str.contains('info/.+?/')] = u'知识首页'
  j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = u'知识列表页'
  j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = u'知识内容页'
  return j['type'].value_counts()

counts2 = [count107(i) for i in sql] #逐块统计
counts2 = pd.concat(counts2).groupby(level=0).sum() #合并统计结果
ratio= counts2/counts2.sum()
pd.DataFrame([counts2,ratio]).T

#其他页面分析
count3=[i[['fullURL']][i['fullURLId'].str.contains('199')].copy() for i in sql] #找出类别为199的网址
def count(a,num):
    b = [a.iloc[i,0].encode('utf-8').split('/') for i in range(a.size)]
    return pd.Series([x[num] for x in b]).value_counts()

c = [count(a,3) for a in count3]
d = pd.concat(c).groupby(level=0).sum()

def count_title(i): #自定义统计函数
  j = i[['pageTitle']][i['fullURLId'].str.contains('199')].copy() #找出类别包含107的网址
  return j['pageTitle'].value_counts()
    
counts4 = [count_title(i) for i in sql] #逐块统计
counts4 = pd.concat(counts4).groupby(level=0).sum() #合并统计结果
print counts4.sort_values( ascending = False)[:5]
pd.DataFrame([counts4,ratio]).T[:5]
pd.sort()

#瞎逛统计
counts5 = [ i['fullURLId'][(i['fullURL'].str.contains('html'))==0].value_counts() for i in sql]
counts5= pd.concat(counts5).groupby(level=0).sum()   
counts5 = pd.DataFrame(counts5)  
counts5['type'] = counts5.index.str.extract('(\d{3})') #提取前三个数字作为类别id
counts5_ = counts5[['type', 'fullURLId']].groupby('type').sum()#按类别合并
counts5_['ratio']=counts5_/counts5_.sum() #增加比例列
counts5_.sort('fullURLId', ascending = False) #按类型编码顺序排序        

#点击次数统计
c = [i['realIP'].value_counts() for i in sql] #统计各个IP出现次数
count6 = pd.concat(c).groupby(level=0).sum()  #合并统计结果
count6 = pd.DataFrame(count6) #将Series转为DataFrame
count6[1] = 1 #添加一列全为1
count6_=count6.groupby('realIP').sum() #统计各个不同点击数 出现的次数
count6_['ratio1']=count6_[1]/count6_[1].sum()
count6_['ratio2']=count6_[1]*count6_.index/(count6_[1]*count6_.index).sum()
count6_.head(10)
count6_.tail(10)

f1 = lambda x : x>=8 and x<=100
f2 = lambda x : x>100 and x<=1000
count6_['index']=count6_.index
count6_[count6_['index'].apply(f1)].sum()
count6_[count6_['index'].apply(f2)].sum()
count6_[count6_['index']>1000].sum()


#浏览一次的用户行为分析

#网页排名

###数据预处理###
#数据清洗
for i in sql:
  d = i[['realIP', 'fullURL']] #只要网址列
  d = d[d['fullURL'].str.contains('\.html')].copy() #只要含有.html的网址
  #保存到数据库的cleaned_gzdata表中（如果表不存在则自动创建）
  d.to_sql('cleaned_gzdata', engine, index = False, if_exists = 'append')
  
#数据变换
for i in sql: #逐块变换并去重
  d = i.copy()
  d['fullURL'] = d['fullURL'].str.replace('_\d{0,2}.html', '.html') #将下划线后面部分去掉，规范为标准网址
  d = d.drop_duplicates() #删除重复记录
  d.to_sql('changed_gzdata', engine, index = False, if_exists = 'append') #保存

#网站分类
for i in sql: #逐块变换并去重
  d = i.copy()
  d['type_1'] = d['fullURL'] #复制一列
  d['type_1'][d['fullURL'].str.contains('(ask)|(askzt)')] = 'zixun' #将含有ask、askzt关键字的网址的类别一归为咨询（后面的规则就不详细列出来了，实际问题自己添加即可）
  d.to_sql('splited_gzdata', engine, index = False, if_exists = 'append') #保存

###模型构建###
import numpy as np

def Jaccard(a, b): #自定义相似系数
  return 1.0*(a*b).sum()/(a+b-a*b).sum()

class Recommender():
  
  sim = None #相似度矩阵
  
  def similarity(self, x, distance): #计算相似度矩阵的函数
    y = np.ones((len(x), len(x)))
    for i in range(len(x)):
      for j in range(len(x)):
        y[i,j] = distance(x[i], x[j])
    return y
  
  def fit(self, x, distance = Jaccard): #训练函数
    self.sim = self.similarity(x, distance)
  
  def recommend(self, a): #推荐函数
    return np.dot(self.sim, a)*(1-a)  





####################################################################################################
####################################################################################################
####################################################################################################


header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('D:/tmp/ml-100k/u.data', sep='\t', names=header)
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print 'Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items)

from sklearn import cross_validation as cv
train_data,test_data = cv.train_test_split(df, test_size = 0.25)

train_data_matrix = np.zeros((n_users,n_items))
for line in train_data.itertuples():
    train_data_matrix[line[1]-1, line[2]-1] = line[3]
    test_data_matrix = np.zeros((n_users, n_items))
for line in test_data.itertuples():
    test_data_matrix[line[1]-1, line[2]-1] = line[3]

from sklearn.metrics.pairwise import pairwise_distances
user_similarity = pairwise_distances(train_data_matrix, metric = "cosine")
item_similarity = pairwise_distances(train_data_matrix.T, metric = "cosine")

def predict(rating, similarity, type = 'user'):
    if type == 'user':
        mean_user_rating = rating.mean(axis = 1)
        rating_diff = (rating - mean_user_rating[:,np.newaxis])
        pred = mean_user_rating[:,np.newaxis] + similarity.dot(rating_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = rating.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred

item_prediction = predict(train_data_matrix, item_similarity, type = 'item')
user_prediction = predict(train_data_matrix, user_similarity, type = 'user')

####################################################################################################

data = [ i[['realIP', 'fullURL']] for i in sql]
data = pd.concat(data)

###探索分析###
#网页类型分析
counts = data.groupby(level=0).sum() #合并统计结果，把相同的统计项合并（即按index分组并求和）
counts = counts.reset_index() #重新设置index，将原来的index作为counts的一列。
counts.columns = ['index', 'num'] #重新设置列名，主要是第二列，默认为0
counts['type'] = counts['index'].str.extract('(\d{3})') #提取前三个数字作为类别id
counts_ = counts[['type', 'num']].groupby('type').sum()#按类别合并
counts_['ratio']=counts_/counts_.sum() #增加比例列
counts_.sort('num', ascending = False) #按类型编码顺序排序

#统计101类别的情况
counts_101=counts[counts['type']=='101'][['index', 'num']]
counts_101['ratio']=counts_101['num']/counts_101['num'].sum()
counts_101.sort('num', ascending = False)


####################################################################################################
####################################################################################################
####################################################################################################

