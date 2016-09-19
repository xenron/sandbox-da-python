# -*- coding: utf-8 -*-

# 对train.csv 的数据进行文本聚类，并且计算聚类的正确率
# 数据是来自不同新闻主题的新闻报道，尝试对数据进行聚类分析，看能不能把不同主题的新闻区分出来

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecs
from scipy import ndimage
from sklearn import manifold, datasets, metrics, feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer 
import jieba
import jieba.posseg
import jieba.analyse

####第一步 计算TFIDF####
    
#文档预料 空格连接
corpus = []
    
#读取预料 一行预料为一个文档
texts=pd.read_csv('d:/tmp/train.csv',encoding="gb18030")
# texts=pd.read_csv('d:/tmp/train.csv',encoding="utf-8")
texts['label']=texts['type']
#label_dict = pd.unique(texts['type'])
#label_dict.to_dict()

label_dict={'auto':1, 'finance':2, 'IT':3, 'health':4, 'sports':5,
            'travel':6, 'education':7, 'jobs':8, 'culture':9, 'military':10}
texts = texts.replace({"label": label_dict})
#texts['jieba'] = " ".join(jieba.cut(texts['text'] ,cut_all=False))

for line in texts['text']:
#for line in open('d:/data/train.csv', 'r').readlines():
#    print line
    # corpus.append(line.strip())
    seg_list = jieba.cut(line ,cut_all=False)
    corpus.append(" ".join(seg_list))

#print corpus
#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()

#该类会统计每个词语的tf-idf权值
transformer = TfidfTransformer()

#第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

#获取词袋模型中的所有词语  
word = vectorizer.get_feature_names()
    
#将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()

#打印特征向量文本内容
print( 'Features length:'+str(len(word)))
#resName = "BHTfidf_Result.txt"
#result = codecs.open(resName, 'w', 'utf-8')
#for j in range(len(word)):
#    result.write(word[j] + ' ')
#result.write('\r\n\r\n')

#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
#for i in range(len(weight)):
#    #print u"-------这里输出第", i, u"类文本的词语tf-idf权重------"  
#    for j in range(len(word)):
#        #print weight[i][j],
#        result.write(str(weight[i][j]) + ' ')
#    result.write('\r\n\r\n')
#
#result.close()


####第二步 聚类Kmeans####
print ('Start Kmeans:')
from sklearn.cluster import KMeans
clf = KMeans(n_clusters=10)   #auto, finance, IT, ..., culture, military
s = clf.fit(weight)
print(s)


#中心点
print(clf.cluster_centers_)
    
#每个样本所属的簇
label = []               #存储100个类标 10个类
print(clf.labels_)
i = 1
while i <= len(clf.labels_):
    print (i, clf.labels_[i-1])
    label.append(clf.labels_[i-1])
    i = i + 1

#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数  958.137281791
print(clf.inertia_)

range(1,101)

m_precision = metrics.precision_score(texts['label'],clf.labels_)
m_recall = metrics.recall_score(texts['label'],clf.labels_)
print 'predict info:'
print 'precision:{0:.3f}'.format(m_precision)
print 'recall:{0:0.3f}'.format(m_recall)
print 'f1-score:{0:.3f}'.format(metrics.f1_score(texts['label'],clf.labels_))
