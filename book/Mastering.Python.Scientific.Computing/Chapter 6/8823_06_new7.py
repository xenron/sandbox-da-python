from sympy import *
x, y, z = symbols('x,y,z')
init_printing(use_unicode=False, wrap_line=False, no_global=True)

f = 4*x**2 + 8*x + 5
g = 3*x + 1
q, r = div(f, g, domain='QQ')
q
r
(q*g + r).expand()
q, r = div(f, g, domain='ZZ')
q
r
g = 4*x + 2
q, r = div(f, g, domain='ZZ')
q
r
(q*g + r).expand()
g = 5*x + 1
q, r = div(f, g, domain='ZZ')
q
r
(q*g + r).expand()
a, b, c = symbols('a,b,c')
f = a*x**2 + b*x + c
g = 3*x + 2
q, r = div(f, g, domain='QQ')
q
r