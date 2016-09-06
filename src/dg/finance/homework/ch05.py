# -*- coding: utf-8 -*-

import scipy.integrate as sci
import sympy as sy
import numpy as np

a, x = sy.symbols('a x')
int_func = sy.Integral(1/(a ** 2 + x ** 2), (x, np.sqrt(3)*a))
print sy.pretty(int_func)


def f2(x):
    return np.sqrt(2 - x ** 2)
a = 0
b = np.sqrt(2)
sci.fixed_quad(f2, a, b)[0]


def f3(x):
    return 1/(x ** 2 * np.sqrt(1 + x ** 2))
a = 1
b = np.sqrt(3)
sci.fixed_quad(f3, a, b)[0]


def f4(x):
    return np.sin(x)/(x ** 2 + 1)
a = -1
b = 1
sci.fixed_quad(f4, a, b)[0]



from math import sqrt
import scipy.optimize as spo
import numpy as np

def Eu((s, b)):
    return -(0.5 * sqrt(s * 15 + b * 12) + 0.5 * sqrt(s * 10 + b * 15))
# 约束
cons = ({'type': 'ineq', 'fun': lambda (s, b):  1000 - s * 8 - b * 10})
# 可接受区间
bnds = ((0, 1000), (0, 1000))
result = spo.minimize(Eu, [5, 5], method='SLSQP', bounds=bnds, constraints=cons)
result
result['x']

