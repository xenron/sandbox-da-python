from sympy.physics.hydrogen import E_nl, E_nl_dirac, R_nl
from sympy import var

var("n Z")
var("r Z")
var("n l")

E_nl(n, Z)
E_nl(1)
E_nl(2, 4)

E_nl(n, l)
E_nl_dirac(5, 2) # l should be less than n
E_nl_dirac(2, 1)
E_nl_dirac(3, 2, False)

R_nl(5, 0, r) # z = 1 by default
R_nl(5, 0, r, 1) 