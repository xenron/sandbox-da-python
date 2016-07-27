from sympy.physics.secondquant import Dagger, B, Bd
from sympy.functions.special.tensor_functions import KroneckerDelta
from sympy.physics.secondquant import B, BKet, FockStateBosonKet
from sympy.abc import x, y, n
from sympy.abc import i, j, k
from sympy import Symbol
from sympy import I

Dagger(2*I)
Dagger(B(0))
Dagger(Bd(0))

KroneckerDelta(1, 2)
KroneckerDelta(3, 3)

#predefined symbols are available in abc including greek symbols like theta
KroneckerDelta(i, j)
KroneckerDelta(i, i)
KroneckerDelta(i, i + 1)
KroneckerDelta(i, i + 1 + k)


a = Symbol('a', above_fermi=True)
i = Symbol('i', below_fermi=True)
p = Symbol('p')
q = Symbol('q')
KroneckerDelta(p, q).indices_contain_equal_information
KroneckerDelta(p, q+1).indices_contain_equal_information
KroneckerDelta(i, p).indices_contain_equal_information

KroneckerDelta(p, a).is_above_fermi
KroneckerDelta(p, i).is_above_fermi
KroneckerDelta(p, q).is_above_fermi


KroneckerDelta(p, a).is_only_above_fermi
KroneckerDelta(p, q).is_only_above_fermi
KroneckerDelta(p, i).is_only_above_fermi



B(x).apply_operator(y)
y*AnnihilateBoson(x)
B(0).apply_operator(BKet((n,)))
sqrt(n)*FockStateBosonKet((n - 1,))