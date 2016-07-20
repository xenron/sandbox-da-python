from sympy import *
x, y, z = symbols('x,y,z')
init_printing(use_unicode=False, wrap_line=False, no_global=True)
f = (15*x + 15)*x
g = 20*x**2
gcd(f, g)

f = 4*x**2/2
g = 16*x/4
gcd(f, g)

f = x*y/3 + y**2
g = 4*x + 9*y
gcd(f, g)

f = x*y**2 + x**2*y
g = x**2*y**2
gcd(f, g)

lcm(f, g)
(f*g).expand()
(gcd(f, g, x, y)*lcm(f, g, x, y)).expand()

f = 4*x**2 + 6*x**3 + 3*x**4 + 2*x**5
sqf_list(f)
sqf(f)

factor(x**4/3 + 6*x**3/16 - 2*x**2/4)
factor(x**2 + 3*x*y + 4*y**2)
