# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 16:46:53 2016

@author: Administrator
"""

import numpy as np
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3

#加载影片数据
titles = open('d:/data/title_list.txt').read().split('\n')
titles = titles[:100]
print titles[:10] #前 10 个片名

links = open('d:/data/link_list_imdb.txt').read().split('\n')
links = links[:100]

synopses_wiki = open('d:/data/synopses_list_wiki.txt').read().split('\n BREAKS HERE')
synopses_wiki = synopses_wiki[:100]

#数据清洗，获取html代码中的文本内容
synopses_clean_wiki = []
for text in synopses_wiki:
    text = BeautifulSoup(text, 'lxml').getText()
    #strips html formatting and converts to unicode
    synopses_clean_wiki.append(text)
    
synopses_wiki = synopses_clean_wiki

genres = open('d:/data/genres_list.txt').read().split('\n')
genres = genres[:100]

print(str(len(titles)) + ' titles')
print(str(len(links)) + ' links')
print(str(len(synopses_wiki)) + ' synopses')
print(str(len(genres)) + ' genres')

synopses_imdb = open('d:/data/synopses_list_imdb.txt').read().split('\n BREAKS HERE')
synopses_imdb = synopses_imdb[:100]

synopses_clean_imdb = []

for text in synopses_imdb:
    text = BeautifulSoup(text, 'html.parser').getText()
    #strips html formatting and converts to unicode
    synopses_clean_imdb.append(text)

synopses_imdb = synopses_clean_imdb


synopses = []

for i in range(len(synopses_wiki)):
    item = synopses_wiki[i] + synopses_imdb[i]
    synopses.append(item)
    
#为每个项目生成索引的全集(在本例中它只是排名),以后我将使用这个得分
ranks = []

for i in range(0,len(titles)):
    ranks.append(i)    
    
# 载入 nltk 的英文停用词作为“stopwords”变量
stopwords = nltk.corpus.stopwords.words('english')
print stopwords[:10]

# 载入 nltk 的 SnowballStemmer 作为“stemmer”变量
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

# 这里定义了一个分词器（tokenizer）和词干分析器（stemmer），它们会输出给定文本词干化后的词集合

def tokenize_and_stem(text):
    # 首先分句，接着分词，而标点也会作为词例存在
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # 过滤所有不含字母的词例（例如：数字、纯标点）
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # 首先分句，接着分词，而标点也会作为词例存在
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # 过滤所有不含字母的词例（例如：数字、纯标点）
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens
    

# 扩充列表后变成了非常庞大的二维（flat）词汇表
totalvocab_stemmed = []
totalvocab_tokenized = []
for i in synopses:
    allwords_stemmed = tokenize_and_stem(i) #对每个电影的剧情简介进行分词和词干化
    totalvocab_stemmed.extend(allwords_stemmed) # 扩充“totalvocab_stemmed”列表

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)
    
vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print 'there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame'


print vocab_frame.head()

# 定义向量化参数
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

%time tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) # 向量化剧情简介文本

print(tfidf_matrix.shape)

terms = tfidf_vectorizer.get_feature_names()

from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)


##k-means聚类
from sklearn.cluster import KMeans
num_clusters = 5
km = KMeans(n_clusters=num_clusters)
%time km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

from sklearn.externals import joblib

# 注释语句用来存储你的模型
# 因为我已经从 pickle 载入过模型了
#joblib.dump(km,  'doc_cluster.pkl')

km = joblib.load('doc_cluster.pkl')
clusters = km.labels_.tolist()

films = { 'title': titles, 'rank': ranks, 'synopsis': synopses, 'cluster': clusters, 'genre': genres }
frame = pd.DataFrame(films, index = [clusters] , columns = ['rank', 'title', 'cluster', 'genre'])
frame['cluster'].value_counts()

grouped = frame['rank'].groupby(frame['cluster']) # 为了凝聚（aggregation），由聚类分类。

grouped.mean() # 每个聚类的平均排名（1 到 100）

from __future__ import print_function

print("Top terms per cluster:")
print()
# 按离质心的距离排列聚类中心，由近到远
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')

    for ind in order_centroids[i, :6]: # 每个聚类选 6 个词
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print() # 空行
    print() # 空行

    print("Cluster %d titles:" % i, end='')
    for title in frame.ix[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print() # 空行
    print() # 空行
    
##多维尺度分析MDS    
import os  # 为了使用 os.path.basename 函数
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.manifold import MDS
MDS()
# 将二位平面中绘制的点转化成两个元素（components）
# 设置为“precomputed”是因为我们提供的是距离矩阵
# 我们可以将“random_state”具体化来达到重复绘图的目的
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)  # 形如 (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]


##可视化聚类
# 用字典设置每个聚类的颜色
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}
# 用字典设置每个聚类名称
cluster_names = {0: 'Family, home, war', 
                 1: 'Police, killed, murders', 
                 2: 'Father, New York, brothers', 
                 3: 'Dance, singing, love', 
                 4: 'Killed, soldiers, captain'}
                 
# 在 ipython 中内联（inline）演示 matplotlib 绘图
%matplotlib inline 

# 用 MDS 后的结果加上聚类编号和绘色创建 DataFrame
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=titles)) 

# 聚类归类
groups = df.groupby('label')


# 设置绘图
fig, ax = plt.subplots(figsize=(17, 9)) # 设置大小
ax.margins(0.05) # 可选项，只添加 5% 的填充（padding）来自动缩放（auto scaling）。

# 对聚类进行迭代并分布在绘图上
# 我用到了 cluster_name 和 cluster_color 字典的“name”项，这样会返回相应的 color 和 label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
            label=cluster_names[name], color=cluster_colors[name], 
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params(
        axis= 'x',          # 使用 x 坐标轴
        which='both',      # 同时使用主刻度标签（major ticks）和次刻度标签（minor ticks）
        bottom='off',      # 取消底部边缘（bottom edge）标签
        top='off',         # 取消顶部边缘（top edge）标签
        labelbottom='off')
    ax.tick_params(
        axis= 'y',         # 使用 y 坐标轴
        which='both',      # 同时使用主刻度标签（major ticks）和次刻度标签（minor ticks）
        left='off',      # 取消底部边缘（bottom edge）标签
        top='off',         # 取消顶部边缘（top edge）标签
        labelleft='off')

ax.legend(numpoints=1)  # 图例（legend）中每项只显示一个点

# 在坐标点为 x,y 处添加影片名作为标签（label）
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)  

plt.show() # 展示绘图

# 以下注释语句可以保存需要的绘图
#plt.savefig('clusters_small_noaxes.png', dpi=200)

plt.close()


##层次聚类
from scipy.cluster.hierarchy import ward, dendrogram
linkage_matrix = ward(dist) # 聚类算法处理之前计算得到的距离，用 linkage_matrix 表示
fig, ax = plt.subplots(figsize=(15, 20)) # 设置大小
ax = dendrogram(linkage_matrix, orientation="right", labels=titles);
plt.tick_params(
        axis= 'x',          # 使用 x 坐标轴
        which='both',      # 同时使用主刻度标签（major ticks）和次刻度标签（minor ticks）
        bottom='off',      # 取消底部边缘（bottom edge）标签
        top='off',         # 取消顶部边缘（top edge）标签
    labelbottom='off')

plt.tight_layout() # 展示紧凑的绘图布局
# 注释语句用来保存图片
plt.savefig('ward_clusters.png', dpi=200) # 保存图片为 ward_clusters

plt.close()                 