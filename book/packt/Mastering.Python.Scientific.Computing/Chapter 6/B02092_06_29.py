from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import (parse_expr,standard_transformations, function_exponentiation)
from sympy.parsing.sympy_parser import (parse_expr,standard_transformations, implicit_multiplication_application)

x = Symbol('x')
parse_expr("2*x**2+3*x+4"))

parse_expr("10*sin(x)**2 + 3xyz")

transformations = standard_transformations + (function_exponentiation,)
parse_expr('10sin**2 x**2 + 3xyz + tan theta', transformations=transformations)

parse_expr("5sin**2 x**2 + 6abc + sec theta",transformations=(standard_transformations +(implicit_multiplication_application,)))
