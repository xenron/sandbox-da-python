from sympy.logic.boolalg import ITE, And, Xor, Or
from sympy.logic.boolalg import to_cnf, to_dnf
from sympy.logic.boolalg import is_cnf, is_dnf
from sympy.abc import A, B, C
from sympy.abc import X, Y, Z
from sympy.abc import a, b, c

ITE(True, False, True)
ITE(Or(True, False), And(True, True), Xor(True, True))
ITE(a, b, c)
ITE(True, a, b)
ITE(False, a, b)
ITE(a, b, c)

to_cnf(~(A | B) | C)
to_cnf((A | B) & (A | ~A), True)

to_dnf(Y & (X | Z))
to_dnf((X & Y) | (X & ~Y) | (Y & Z) | (~Y & Z), True)

is_cnf(X | Y | Z)
is_cnf(X & Y & Z)
is_cnf((X & Y) | Z)
is_cnf(X & (Y | Z))

is_dnf(X | Y | Z)
is_dnf(X & Y & Z)
is_dnf((X & Y) | Z)
is_dnf(X & (Y | Z))