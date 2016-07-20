from sympy.interactive import init_printing
from sympy import Symbol, sqrt
from sympy.abc import x, y
sqrt(21)
init_printing(pretty_print=True) 
sqrt(21) 
theta = Symbol('theta') 
init_printing(use_unicode=True) 
theta 
init_printing(use_unicode=False) 
theta 
init_printing(order='lex') 
str(2*y + 3*x + 2*y**2 + x**2+1) 
init_printing(order='grlex') 
str(2*y + 3*x + 2*y**2 + x**2+1) 
init_printing(order='grevlex') 
str(2*y * x**2 + 3*x * y**2) 
init_printing(order='old') 
str(2*y + 3*x + 2*y**2 + x**2+1) 
init_printing(num_columns=10) 
str(2*y + 3*x + 2*y**2 + x**2+1) 