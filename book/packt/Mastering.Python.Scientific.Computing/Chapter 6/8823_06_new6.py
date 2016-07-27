from sympy import integrate, log, exp, oo
from sympy.abc import n, x, y
from sympy import sqrt
from sympy import *
integrate(x*y, x)
integrate(log(x), x)
integrate(log(x), (x, 1, n))
integrate(x)
integrate(sqrt(1 + x), (x, 0, x))
integrate(sqrt(1 + x), x)
integrate(x*y)
integrate(x**n*exp(-x), (x, 0, oo)) # same as conds='piecewise'
integrate(x**n*exp(-x), (x, 0, oo), conds='none')
integrate(x**n*exp(-x), (x, 0, oo), conds='separate')
init_printing(use_unicode=False, wrap_line=False, no_global=True)
x = Symbol('x')
integrate(x**3 + x**2 + 1, x)
integrate(x/(x**3+3*x+1), x)
integrate(x**3 * exp(x) * cos(x), x)
integrate(exp(-x**3)*erf(x), x)