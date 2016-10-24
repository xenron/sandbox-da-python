# -*- coding: utf-8 -*-

# 作业1 数据集中提供了汽车销售行业纳税人的各个属性与是否偷漏税标识。
# 请结合汽车销售行业纳税人的各个属性，总结衡量纳税人的经营特征，建立偷漏税行为识别模型，识别偷漏税纳税人


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


data=pd.read_excel('d:/tmp/1.xls',index_col=0)
print(data.head())
data.ix[:,0:14]
#data.columns
#
#data[:'输出']
## data.columns = ['type','mode'] + data.columns[2:len(data.columns)]
#data.astype(object)
#data.ix[:,0:1] = data.ix[:,0:1].astype(object)
#data.ix[:,0:1].columns
##
##data.head()
##data.columns[2:4]
##data = pd.DataFrame(data)
#
#data['type'] = pd.Categorical.from_array(data.ix[:,0:1]).labels
#data[:,1:3]
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

#datafile = 'd:/data/example/model.xls' #数据名
#data = pd.read_excel(datafile) #读取数据，数据的前三列是特征，第四列是标签
#data["Loan_Status_Coded"] = coding(data["Loan_Status"], {'N':0,'Y':1})
data = data.as_matrix() #将表格转换为矩阵
shuffle(data) #随机打乱数据

p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:] #前80%为训练集
test = data[int(len(data)*p):,:] #后20%为测试集

#构建CART决策树模型
from sklearn.tree import DecisionTreeClassifier #导入决策树模型

#treefile = 'd:/data/example/tree.pkl' #模型输出名字
tree = DecisionTreeClassifier() #建立决策树模型
tree.fit(train[:,:14], train[:,14]) #训练

#保存模型
#from sklearn.externals import joblib
#joblib.dump(tree, treefile)


cm_plot(train[:,14], tree.predict(train[:,:14])).show() #显示混淆矩阵可视化结果
#注意到Scikit-Learn使用predict方法直接给出预测结果。

from sklearn.metrics import roc_curve #导入ROC曲线函数

fpr, tpr, thresholds = roc_curve(test[:,14], tree.predict_proba(test[:,:14])[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of CART', color = 'green') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show() #显示作图结果

