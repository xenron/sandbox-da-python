from sympy import together, apart, symbols
from sympy import *

x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
x1/x2 + x3/x4
together(x1/x2 + x3/x4)


apart ((2*x**2+3*x+4)/(x+1))
together(apart ((2*x**2+3*x+4)/(x+1)))

log(4).n()
log(4,4).n()
ln(4).n()
mpmath.log10(4)