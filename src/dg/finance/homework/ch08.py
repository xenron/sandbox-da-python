# -*- coding: utf-8 -*-


#协方差矩阵
import numpy as np
X = [[2, 0, -1.4],
[2.2, 0.2, -1.5],
[2.4, 0.1, -1],
[1.9, 0, -1.2]]
print(np.cov(np.array(X).T))

#特征值与特征向量
w, v = np.linalg.eig(np.array([[1, -2], [2, -3]]))
print('特征值：{}\n特征向量：{}'.format(w,v))

#使用PCA降维
import pandas as pd
x1=[0.9,2.4,1.2,0.5,0.3,1.8,0.5,0.3,2.5,1.3]
x2=[1,2.6,1.7,0.7,0.7,1.4,0.6,0.6,2.6,1.1]
data=pd.DataFrame([x1,x2],index=['x1','x2'])


data_new=(data.T-np.mean(data,axis=1)).T

a, b = np.linalg.eig(np.cov(data_new))

np.dot(data_new.T,b[:,0])


#鸢尾花数据集的降维
%matplotlib inline
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
y = data.target
X = data.data
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()

###构造PCA指数
import pandas as pd
from datetime import datetime 
import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA
import pandas_datareader.data as web

symbols = ['ADS.DE', 'ALV.DE', 'BAS.DE', 'BAYN.DE', 'BEI.DE',
           'BMW.DE', 'CBK.DE', 'CON.DE', 'DAI.DE', 'DB1.DE',
           'DBK.DE', 'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FME.DE',
           'FRE.DE', 'HEI.DE', 'HEN3.DE', 'IFX.DE', 'LHA.DE',
           'LIN.DE', 'LXS.DE', 'MRK.DE', 'MUV2.DE', 'RWE.DE',
           'SAP.DE', 'SDF.DE', 'SIE.DE', 'TKA.DE', 'VOW3.DE',
           '^GDAXI']
           
get_ipython().run_cell_magic(u'time', u'', u"data = pd.DataFrame()\nfor sym in symbols:\n    data[sym] = web.DataReader(sym, data_source='yahoo')['Close']\ndata = data.dropna()")

dax = pd.DataFrame(data.pop('^GDAXI'))           

data[data.columns[:6]].head()

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
plt.scatter(dax['PCA_5'], dax['^GDAXI'], c=mpl_dates)
lin_reg = np.polyval(np.polyfit(dax['PCA_5'],
                                dax['^GDAXI'], 1),
                                dax['PCA_5'])
plt.plot(dax['PCA_5'], lin_reg, 'r', lw=3)
plt.grid(True)
plt.xlabel('PCA_5')
plt.ylabel('^GDAXI')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
                format=mpl.dates.DateFormatter('%d %b %y'))
                
cut_date = '2011/7/1'
early_pca = dax[dax.index < cut_date]['PCA_5']
early_reg = np.polyval(np.polyfit(early_pca,
                dax['^GDAXI'][dax.index < cut_date], 1),
                early_pca)

late_pca = dax[dax.index >= cut_date]['PCA_5']
late_reg = np.polyval(np.polyfit(late_pca,
                dax['^GDAXI'][dax.index >= cut_date], 1),
                late_pca)


plt.figure(figsize=(8, 4))
plt.scatter(dax['PCA_5'], dax['^GDAXI'], c=mpl_dates)
plt.plot(early_pca, early_reg, 'r', lw=3)
plt.plot(late_pca, late_reg, 'r', lw=3)
plt.grid(True)
plt.xlabel('PCA_5')
plt.ylabel('^GDAXI')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
                format=mpl.dates.DateFormatter('%d %b %y'))                
