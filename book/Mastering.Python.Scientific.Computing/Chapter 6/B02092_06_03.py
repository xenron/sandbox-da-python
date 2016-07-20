from sympy import collect, expand, factor, simplify, subs
from sympy import Symbol, symbols
from sympy import sin, cos

x, y, a, b, c, d = symbols('x y a b')

expr = a*x**2+2*b*x**2+cos(x)+51*x**2
simplify(expr)

factor(x**2+x-30)
expand ( (x-5) * (x+6) )

collect(x**3 + a*x**2 + b*x**2 + c*x + d, x)

expr = sin(x)*sin(x) + cos(x)*cos(x)
expr
expr.subs({x:5, y:25})
expr.subs({x:5, y:25}).n()