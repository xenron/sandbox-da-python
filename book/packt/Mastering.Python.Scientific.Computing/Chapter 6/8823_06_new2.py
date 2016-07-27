from sympy.logic.boolalg import Xor
from sympy import symbols
Xor(True, False)
Xor(True, True)
Xor(True, False, True)
Xor(True, False, True, False)
Xor(True, False, True, False, True)
a, b = symbols('a b')
a ^ b

from sympy.logic.boolalg import Nand
Nand(True, False)
Nand(True, True)
Nand(a, b)

from sympy.logic.boolalg import Nor
Nor(True, False)
Nor(True, True)
Nor(False, True)
Nor(False, False)
Nor(a, b)

from sympy.logic.boolalg import Equivalent, And
Equivalent(False, False, False)
Equivalent(True, False, False)
Equivalent(a, And(a, True))

from sympy.logic.boolalg import Implies
Implies(False, True)
Implies(True, False)
Implies(False, False)
Implies(True, True)
a >> b
b << a