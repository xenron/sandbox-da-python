#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]


if __name__ == "__main__":
    path = u'..\\算法讲师\\机器学习升级版\\数据\\4.2.iris.data'  # 数据文件路径

    # 路径，浮点型数据，逗号分隔，第4列使用函数iris_type单独处理
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})

    # 将数据的0到3列组成x，第4列得到y
    x, y = np.split(data, (4,), axis=1)

    # 为了可视化，仅使用前两列特征
    x = x[:, :2]

    # print x
    # print y

    logreg = LogisticRegression()   # Logistic回归模型
    logreg.fit(x, y.ravel())        # 根据数据[x,y]，计算回归参数

    # 画图
    N, M = 500, 500     # 横纵各采样多少个值
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()   # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()   # 第1列的范围
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)                    # 生成网格采样点
    x_test = np.stack((x1.flat, x2.flat), axis=1)   # 测试点

    # # 无意义，只是为了凑另外两个维度
    # x3 = np.ones(x1.size) * np.average(x[:, 2])
    # x4 = np.ones(x1.size) * np.average(x[:, 3])
    # x_test = np.stack((x1.flat, x2.flat, x3, x4), axis=1)  # 测试点

    y_hat = logreg.predict(x_test)                  # 预测值
    y_hat = y_hat.reshape(x1.shape)                 # 使之与输入的形状相同
    plt.pcolormesh(x1, x2, y_hat, cmap=plt.cm.Spectral, alpha=0.1)  # 预测值的显示Paired/Spectral/coolwarm/summer/spring/OrRd/Oranges
    plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', cmap=plt.cm.prism)  # 样本的显示
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid()
    plt.show()

    # 训练集上的预测结果
    y_hat = dt_clf.predict(x)
    y = y.reshape(-1)       # 此转置仅仅为了print时能够集中显示
    print y_hat.shape       # 不妨显示下y_hat的形状
    print y.shape
    result = (y_hat == y)   # True则预测正确，False则预测错误
    print y_hat
    print y
    print result
    c = np.count_nonzero(result)    # 统计预测正确的个数
    print c
    print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))
