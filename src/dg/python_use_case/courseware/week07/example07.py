# -*- coding: utf-8 -*-

###随机性检验###
from scipy.stats import chisquare 
import numpy as np
import pandas as pd 
def randomtest(data):
    N=len(data)
    data=pd.Series(data)
    if(N<30):
        R=np.nan
        return R
    else:
        p = [0.1*N]*10
        ni=np.zeros([10])
        for i in range(10):
            ni[i] = len(data[data==i])
        p_value = chisquare(ni, p)[1]  
        if(p_value>=0.05):
            R = 0
            return R
        else:
            R=1 
            return R
            
###数据集初始化###

#排序
bh1 = pd.read_csv("D:/tmp/bh1.csv",header=None)
#bh1=bh1.ix[:100]
N = bh1.shape[0]
n = bh1.shape[1]

#mark列表
mark=[]
for i in range(n):
    mark.append(np.zeros((N, n)))
regular=[]

##指针初始化
i=0
j=0
a=0
b=N

##循环
while i < n:
    while i <= j and j < n:
        if (mark[i] == 0).all():
            R = randomtest(bh1.iloc[a:b, j])
            if (R == np.nan):
                break
            elif (R == 0):
                i = i + 1
                j = i
                continue
            else:
                mark[i][0, j] = 1
                for c in range(N)[1:]:
                    if bh1.iloc[c, j] != bh1.iloc[c - 1, j]:
                        mark[i][c, j] = 1
#                    else:
#                        mark[i][c,j]=0
                j = j + 1
        if (not (mark[i] == 0).all()):
            if (j < n):
                kj = np.sum(mark[i][:, j - 1] == 1)
                s = bh1[mark[i][:, j - 1] == 1].index
                for k in range(kj):
                    a = s[k]
                    if k == kj - 1:
                        b = N
                    else:
                        b = s[k + 1]
                    R = randomtest(bh1.iloc[a:b, j])
                    if R == 1:
                        mark[i][a, j] = 1
                        for c in range(b)[a + 1:]:
                            if bh1.iloc[c, j] != bh1.iloc[c - 1, j]:
                                mark[i][c, j] = 1
                                if mark[i][c, j - 1] == 0:
                                    mark[i][c, j - 1] = 1
#                                else:
#                                    mark[i][c,j]=0

                    elif R == 0:
                        mark[i][a:b, j] = np.nan
                    else:
                        mark[i][a:b, j:n] = np.nan
                    j = j + 1
    i = i + 1
    j = i
    a = 0
    b = N
    
    
#regular列表
for i in range(n):
    for j in range(n)[i:]:
        a=np.sum(mark[i][:,j]==1)
        regular.append(np.zeros((a,n)))
        for k in range(N):
            if mark[i][k,j]==1:
                regular[i][b,j]=bh1.iloc[k,j]
                b=b+1
            elif mark[i][k,j]==np.nan or mark[i][k,j]==0:
                regular[i][b,j]=np.nan
        

###随机数生成###
from numpy.random import randint
ran=randint(10,size=(N,n))   
ran=pd.DataFrame(ran)                        
                    
ran['class']=0
bh1['class']=1

sample=bh1.append(ran)

#特征提取
for i in range(n):
    for a in range(regular[i].shape[0]):
        loc=regular[i][a,:]!=np.nan
        for b in range(sample.shape[0]):
            if sample.iloc[b,loc]==regular[i][a,loc]:
                sample.iloc[b,'input'+i]=1
            else:sample.iloc[b,'input'+i]=0

#构建分类模型
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB() 
inputs=['input0','input1','input2','input3','input4','input5','input6']
x_train=sample[inputs]
y_train=sample['class']
clf.fit(x_train,y_train)

#预测新数字串
x_test=[1,1,1,0,0,0,0]
clf.predict(x_test)

        

