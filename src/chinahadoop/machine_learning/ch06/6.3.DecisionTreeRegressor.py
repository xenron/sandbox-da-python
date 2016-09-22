#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

if __name__ == "__main__":
    N = 100
    x = np.random.rand(N) * 6 - 3     # [-3,3)
    x.sort()
    y = np.sin(x) + np.random.randn(N) * 0.05
    x = x.reshape(-1, 1)  # 转置后，得到N个样本，每个样本都是1维的

    reg = DecisionTreeRegressor(criterion='mse', max_depth=4)
    dt = reg.fit(x, y)
    x_test = np.linspace(-3, 3, 50).reshape(-1, 1)
    y_hat = dt.predict(x_test)
    plt.plot(x, y, 'r*', linewidth=2, label='Actual')
    plt.plot(x_test, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

    # # 比较决策树的深度影响
    # depth = [2, 4, 6, 8, 10]
    # clr = 'rgmby'
    # reg = [ DecisionTreeRegressor(criterion='mse', max_depth=depth[0]),
    #     DecisionTreeRegressor(criterion='mse', max_depth=depth[1]),
    #     DecisionTreeRegressor(criterion='mse', max_depth=depth[2]),
    #     DecisionTreeRegressor(criterion='mse', max_depth=depth[3]),
    #     DecisionTreeRegressor(criterion='mse', max_depth=depth[4])]
    #
    # plt.plot(x, y, 'ko', linewidth=2, label='Actual')
    # x_test = np.linspace(-3, 3, 50).reshape(-1, 1)
    # for i, r in enumerate(reg):
    #     dt = r.fit(x, y)
    #     y_hat = dt.predict(x_test)
    #     plt.plot(x_test, y_hat, '-', color=clr[i], linewidth=2, label='Depth=%d' % depth[i])
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()
