# -*- coding: utf-8 -*-

# stock_dji.csv(见百度云盘)包含了道琼斯指数的23个成分股数据，dji.csv 道琼斯股票数据
# 使用成分股数据构建出PCA指数，并与道琼斯指数进行比较

# 构造PCA指数
import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from datetime import datetime 
from sklearn.decomposition import KernelPCA

# 读取数据
data = pd.read_csv('d:/tmp/stock_dji.csv', parse_dates=True, index_col=0)
data_DJI = pd.read_csv('d:/tmp/DJI.csv', parse_dates=True, index_col=0)

# 过滤DJI.csv中无效数据
dji_orgi = data_DJI[data_DJI.index.isin(data.index)]
# 只取收盘价格
dji = pd.DataFrame(dji_orgi.pop('Adj Close'))

data.head()
dji.head()

# 标准化数据集
scale_function = lambda x: (x - x.mean()) / x.std()

# 不限制主成分个数
pca = KernelPCA().fit(data.apply(scale_function))
len(pca.lambdas_)

# 前10个主成分
pca.lambdas_[:10].round()

get_we = lambda x: x / x.sum()

get_we(pca.lambdas_)[:10]
# 前N个主成分的方差贡献度（数据变异性）
get_we(pca.lambdas_)[:5].sum()
get_we(pca.lambdas_)[:10].sum()

# 1个主成分
pca_1 = KernelPCA(n_components=1).fit(data.apply(scale_function))
dji['PCA_1'] = pca_1.transform(-data)
# 对比，道琼斯指数和PCA_1指数
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
dji.apply(scale_function).plot(figsize=(8, 4))

# 根据方差贡献度的权重比例，计算前5个主成分得到的加权平均数
pca_5 = KernelPCA(n_components=5).fit(data.apply(scale_function))
pca_components_5 = pca_5.transform(-data)
weights_5 = get_we(pca_5.lambdas_)
dji['PCA_5'] = np.dot(pca_components_5, weights_5)
# 对比，道琼斯指数，PCA_1指数，PCA_5指数
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
dji.apply(scale_function).plot(figsize=(8, 4))

# 根据方差贡献度的权重比例，计算前10个主成分得到的加权平均数
pca_10 = KernelPCA(n_components=10).fit(data.apply(scale_function))
pca_components_10 = pca_10.transform(-data)
weights_10 = get_we(pca_10.lambdas_)
dji['PCA_10'] = np.dot(pca_components_10, weights_10)
# 对比，道琼斯指数，PCA_1指数，PCA_5指数
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
dji.apply(scale_function).plot(figsize=(8, 4))











