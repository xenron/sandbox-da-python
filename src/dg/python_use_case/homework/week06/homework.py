# -*- coding: utf-8 -*-
###数据抽取###
#加载包
import pandas as pd
from sqlalchemy import create_engine

#连接数据库
engine = create_engine('mysql+pymysql://root:root@172.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize = 10000)

import numpy as np
import pandas as pd

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







































