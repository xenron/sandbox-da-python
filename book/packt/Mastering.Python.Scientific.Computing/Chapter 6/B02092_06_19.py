from sympy.physics.qho_1d import E_n, psi_n
from sympy.physics.sho import E_nl, R_nl
from sympy import var

var("x m omega")
var("r nu l")
x, y, z = symbols('x, y, z')

E_n(x, omega)
psi_n(2, x, m, omega)
E_nl(x, y, z)

R_nl(1, 0, 1, r)
R_nl(2, l, 1, r)
