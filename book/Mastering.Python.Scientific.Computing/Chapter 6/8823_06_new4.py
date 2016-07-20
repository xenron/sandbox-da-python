from sympy.logic import simplify_logic
from sympy.abc import x, y, z
from sympy import S

from sympy.logic import SOPform
minterms = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
dontcares = [[1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0]]
SOPform(['w','x','y','z'], minterms, dontcares)

from sympy.logic import POSform
minterms = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
dontcares = [[1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0]]
POSform(['w','x','y','z'], minterms, dontcares)

expr = '(~x & y & ~z) | ( ~x & ~y & ~z)'
simplify_logic(expr)
S(expr)
simplify_logic(_)