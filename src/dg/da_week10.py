# -*- coding: utf-8 -*-
from numpy import *
import pandas as pd
###线性回归####
#读取数据
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

data.head()

data.tail()

#画散点图
import seaborn as sns
import matplotlib

%matplotlib inline

sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.8)

sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')

#计算相关系数矩阵
data.corr()

#构建X、Y数据集
X = data[['TV', 'Radio', 'Newspaper']]
X.head()

y = data['Sales']
y.head()

##直接根据系数矩阵公式计算
def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws


#求解回归方程系数
X2=X
X2['intercept']=[1]*200
standRegres(X2,y)


##利用现有库求解
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()

linreg.fit(X, y)

print linreg.intercept_
print linreg.coef_
print zip(['TV','Radio','Newspaper'], linreg.coef_)

##测试集和训练集的构建
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg.fit(X_train, y_train)
#结果
print linreg.intercept_
print linreg.coef_
print zip(['TV','Radio','Newspaper'], linreg.coef_)

#预测
y_pred = linreg.predict(X_test)

#误差评估
from sklearn import metrics

# calculate MAE using scikit-learn
print "MAE:",metrics.mean_absolute_error(y_test,y_pred)


# calculate MSE using scikit-learn
print "MSE:",metrics.mean_squared_error(y_test,y_pred)


# calculate RMSE using scikit-learn
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred))

##模型比较
feature_cols = ['TV', 'Radio']

X = data[feature_cols]
y = data.Sales

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

linreg.fit(X_train, y_train)

y_pred = linreg.predict(X_test)


# calculate MAE using scikit-learn
print "MAE:",metrics.mean_absolute_error(y_test,y_pred)


# calculate MSE using scikit-learn
print "MSE:",metrics.mean_squared_error(y_test,y_pred)


# calculate RMSE using scikit-learn
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred))
