# -*- coding: utf-8 -*-

from scipy.stats import chisquare 
import numpy as np
import pandas as pd

###数据集初始化###
bh2 = pd.read_csv("D:/tmp/bh2.txt", header=None)
bh2['str'] = bh2[0].astype('str') 

for i in range(9):
    bh2['index' + str(i+1)] = bh2['str'].str[i:i+1]

# 找出第一列的非重复值
bh2['index1'].unique()
# 根据第一列的非重复值，得到各个种类的数量分布
bh2.groupby(['index1']).count()

df = bh2[['index1','index2','index3','index4','index5','index6','index7','index8','index9']]
N = df.shape[0]
n = df.shape[1]

###随机性检验###
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
            R = randomtest(df.iloc[a:b, j])
            if (R == np.nan):
                break
            elif (R == 0):
                i = i + 1
                j = i
                continue
            else:
                mark[i][0, j] = 1
                for c in range(N)[1:]:
                    if df.iloc[c, j] != df.iloc[c - 1, j]:
                        mark[i][c, j] = 1
#                    else:
#                        mark[i][c,j]=0
                j = j + 1
        if (not (mark[i] == 0).all()):
            if (j < n):
                kj = np.sum(mark[i][:, j - 1] == 1)
                s = df[mark[i][:, j - 1] == 1].index
                for k in range(kj):
                    a = s[k]
                    if k == kj - 1:
                        b = N
                    else:
                        b = s[k + 1]
                    R = randomtest(df.iloc[a:b, j])
                    if R == 1:
                        mark[i][a, j] = 1
                        for c in range(b)[a + 1:]:
                            if df.iloc[c, j] != df.iloc[c - 1, j]:
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
                regular[i][b,j]=df.iloc[k,j]
                b=b+1
            elif mark[i][k,j]==np.nan or mark[i][k,j]==0:
                regular[i][b,j]=np.nan
        

###随机数生成###
from numpy.random import randint
ran=randint(10,size=(N,n))   
ran=pd.DataFrame(ran)                        
                    
ran['class']=0
df['class']=1

sample=df.append(ran)

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
x_test=[3,0,2,1,0,9,9,9]
clf.predict(x_test)

        