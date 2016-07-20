from sympy import simplify, cos, sin, trigsimp, cancel
from sympy import sqrt, count_ops, oo, symbols, log
from sympy.abc import x, y

expr = (2*x + 3*x**2)/(4*x*sin(y)**2 + 2*x*cos(y)**2)
expr
simplify(expr)

trigsimp(expr)
cancel(_)

root = 4/(sqrt(2)+3)
simplify(root, ratio=1) == root
count_ops(simplify(root, ratio=oo)) > count_ops(root)
x, y = symbols('x y', positive=True)
expr2 = log(x) + log(y) + log(x)*log(1/y)

expr3 = simplify(expr2)
expr3
count_ops(expr2)
count_ops(expr3)
print(count_ops(expr2, visual=True))
print(count_ops(expr3, visual=True))