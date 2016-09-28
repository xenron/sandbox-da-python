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

data = pd.read_csv('d:/tmp/stock_dji.csv', parse_dates=True, index_col=0)
data_DJI = pd.read_csv('d:/tmp/DJI.csv', parse_dates=True, index_col=0)
dax = data_DJI[data_DJI.index.isin(data.index)]

data.head()
dax.head()

scale_function = lambda x: (x - x.mean()) / x.std()

pca = KernelPCA().fit(data.apply(scale_function))

len(pca.lambdas_)

pca.lambdas_[:10].round()

get_we = lambda x: x / x.sum()

get_we(pca.lambdas_)[:10]

get_we(pca.lambdas_)[:5].sum()

pca = KernelPCA(n_components=1).fit(data.apply(scale_function))
dax['PCA_1'] = pca.transform(-data)

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
dax.apply(scale_function).plot(figsize=(8, 4))



pca = KernelPCA(n_components=5).fit(data.apply(scale_function))
pca_components = pca.transform(-data)
weights = get_we(pca.lambdas_)
dax['PCA_5'] = np.dot(pca_components, weights)

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
dax.apply(scale_function).plot(figsize=(8, 4))

import matplotlib as mpl
mpl_dates = mpl.dates.date2num(data.index.to_pydatetime())
mpl_dates


plt.figure(figsize=(8, 4))
plt.scatter(dax['PCA_5'], dax['Open'], c=mpl_dates)
lin_reg = np.polyval(np.polyfit(dax['PCA_5'],
                                dax['Open'], 1),
                                dax['PCA_5'])
plt.plot(dax['PCA_5'], lin_reg, 'r', lw=3)
plt.grid(True)
plt.xlabel('PCA_5')
plt.ylabel('Open')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
                format=mpl.dates.DateFormatter('%d %b %y'))
                
cut_date = '2011/7/1'
early_pca = dax[dax.index < cut_date]['PCA_5']
early_reg = np.polyval(np.polyfit(early_pca,
                dax['Open'][dax.index < cut_date], 1),
                early_pca)

late_pca = dax[dax.index >= cut_date]['PCA_5']
late_reg = np.polyval(np.polyfit(late_pca,
                dax['Open'][dax.index >= cut_date], 1),
                late_pca)


plt.figure(figsize=(8, 4))
plt.scatter(dax['PCA_5'], dax['Open'], c=mpl_dates)
plt.plot(early_pca, early_reg, 'r', lw=3)
plt.plot(late_pca, late_reg, 'r', lw=3)
plt.grid(True)
plt.xlabel('PCA_5')
plt.ylabel('Open')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
                format=mpl.dates.DateFormatter('%d %b %y'))                
