from sympy import *

x, y = symbols('x y')
expr = sin(x)*cos(y)+cos(x)*sin(y)
expr_exp= exp(5*sin(x)**2+4*cos(x)**2)

trigsimp(expr)
trigsimp(expr_exp)
expand_trig(sin(x+y))
solve(x**2+4,x) #complex number as solution