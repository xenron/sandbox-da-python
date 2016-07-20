from sympy import *

p, q = symbols ('p q')
p = (x+4)*(x+2)
q = x**2 + 6*x + 8
p == q # Unsuccessfull
p - q == 0 # Unsuccessfull 
simplify(p - q) == 0