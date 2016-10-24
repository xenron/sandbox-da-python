# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


###周期性分析###
power=pd.read_csv('d:/data/example/Ele_pow.csv',index_col=0)
print(power.head())
power.plot()

###缺失值处理###
from scipy.interpolate import lagrange #导入拉格朗日插值函数

inputfile = 'd:/data/example/missing_data.xls' #输入数据路径,需要使用Excel格式；
outputfile = 'd:/data/example/missing_data_processed.xls' #输出数据路径,需要使用Excel格式

data = pd.read_excel(inputfile, header=None) #读入数据
data

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
  y = y[y.notnull()] #剔除空值
  return lagrange(y.index, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for i in data.columns:
  for j in range(len(data)):
    if (data[i].isnull())[j]: #如果为空即插值。
      data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile, header=None, index=False) #输出结果


###构建模型####
def cm_plot(y, yp):
  
  from sklearn.metrics import confusion_matrix

  cm = confusion_matrix(y, yp) 
  
  import matplotlib.pyplot as plt 
  plt.matshow(cm, cmap=plt.cm.Greens) 
  plt.colorbar() 
  
  for x in range(len(cm)): 
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
  
  plt.ylabel('True label') 
  plt.xlabel('Predicted label') 
  return plt
  
#构建并测试CART决策树模型

import pandas as pd #导入数据分析库
from random import shuffle #导入随机函数shuffle，用来打算数据

datafile = 'd:/data/example/model.xls' #数据名
data = pd.read_excel(datafile) #读取数据，数据的前三列是特征，第四列是标签
data = data.as_matrix() #将表格转换为矩阵
shuffle(data) #随机打乱数据

p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:] #前80%为训练集
test = data[int(len(data)*p):,:] #后20%为测试集

#构建CART决策树模型
from sklearn.tree import DecisionTreeClassifier #导入决策树模型

treefile = 'd:/data/example/tree.pkl' #模型输出名字
tree = DecisionTreeClassifier() #建立决策树模型
tree.fit(train[:,:3], train[:,3]) #训练

#保存模型
from sklearn.externals import joblib
joblib.dump(tree, treefile)


cm_plot(train[:,3], tree.predict(train[:,:3])).show() #显示混淆矩阵可视化结果
#注意到Scikit-Learn使用predict方法直接给出预测结果。

from sklearn.metrics import roc_curve #导入ROC曲线函数

fpr, tpr, thresholds = roc_curve(test[:,3], tree.predict_proba(test[:,:3])[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of CART', color = 'green') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show() #显示作图结果


#构建神经网络模型
import pandas as pd
from random import shuffle

datafile = 'd:/data/example/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from keras.models import Sequential #导入神经网络初始化函数
from keras.layers.core import Dense, Activation #导入神经网络层函数、激活函数

netfile = 'd:/data/example/net.model' #构建的神经网络模型存储路径

net = Sequential() #建立神经网络
net.add(Dense(10,input_dim=3)) #添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu')) #隐藏层使用relu激活函数
net.add(Dense(1,input_dim=10)) #添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid')) #输出层使用sigmoid激活函数
net.compile(loss = 'binary_crossentropy', optimizer = 'adam') #编译模型，使用adam方法求解

net.fit(train[:,:3], train[:,3], nb_epoch=1000, batch_size=1) #训练模型，循环1000次
net.save_weights(netfile) #保存模型

predict_result = net.predict_classes(train[:,:3]).reshape(len(train)) #预测结果变形
'''这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n'''


cm_plot(train[:,3], predict_result).show() #显示混淆矩阵可视化结果

from sklearn.metrics import roc_curve #导入ROC曲线函数

predict_result = net.predict(test[:,:3]).reshape(len(test))
fpr, tpr, thresholds = roc_curve(test[:,3], predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of LM') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show() #显示作图结果  