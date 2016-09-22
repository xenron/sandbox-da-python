# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from scipy.stats import multivariate_normal
from sklearn.mixture import GMM
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False


if __name__ == '__main__':
    mu1 = (0, 0, 0)
    cov = np.identity(3)
    data1 = np.random.multivariate_normal(mu1, cov, 400)
    mu1 = (2, 2, 1)
    cov = np.identity(3)
    data2 = np.random.multivariate_normal(mu1, cov, 100)
    data = np.vstack((data1, data2))

    num_iter = 100
    n, d = data.shape
    # 随机指定
    # mu1 = np.random.standard_normal(d)
    # mu2 = np.random.standard_normal(d)
    mu1 = data.min(axis=0)
    mu2 = data.max(axis=0)
    sigma1 = np.identity(d)
    sigma2 = np.identity(d)
    pi = 0.5

    # EM
    for i in range(num_iter):
        # E
        norm1 = multivariate_normal(mu1, sigma1)
        norm2 = multivariate_normal(mu2, sigma2)
        tau1 = pi*norm1.pdf(data)
        tau2 = (1-pi)*norm2.pdf(data)
        gamma = tau1 / (tau1 + tau2)

        # M
        mu1 = np.dot(gamma, data)/sum(gamma)
        mu2 = np.dot((1-gamma), data)/sum((1-gamma))
        sigma1 = np.dot(gamma * (data - mu1).T, data - mu1) / np.sum(gamma)
        sigma2 = np.dot((1-gamma) * (data - mu2).T, data - mu2) / np.sum(1-gamma)
        pi = sum(gamma)/n
        if i % 10 == 0:
            print i, ":\t", mu1, mu2

    print '类别概率:\t', pi
    print '均值:\t', mu1, mu2
    print '方差:\n', sigma1, '\n', sigma2, '\n'

    g = GMM(n_components=2, covariance_type='full', n_iter=100)
    g.fit(data)
    print '类别概率:\t', g.weights_[0]
    print '均值:\n', g.means_, '\n'
    print '方差:\n', g.covars_, '\n'

    # 预测分类
    norm1 = multivariate_normal(mu1, sigma1)
    norm2 = multivariate_normal(mu2, sigma2)
    tau1 = norm1.pdf(data)
    tau2 = norm2.pdf(data)

    fig = plt.figure(figsize=(14, 7), facecolor='w')
    ax = fig.add_subplot(121, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='b', s=30, marker='o', depthshade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(u'原始数据', fontsize=18)
    ax = fig.add_subplot(122, projection='3d')
    c1 = tau1 > tau2
    ax.scatter(data[c1, 0], data[c1, 1], data[c1, 2], c='r', s=30, marker='o', depthshade=True)
    c2 = tau1 < tau2
    ax.scatter(data[c2, 0], data[c2, 1], data[c2, 2], c='g', s=30, marker='^', depthshade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(u'EM算法分类', fontsize=18)

    plt.tight_layout()
    plt.show()
