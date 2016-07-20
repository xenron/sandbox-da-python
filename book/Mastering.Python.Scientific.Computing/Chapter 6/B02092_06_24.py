from sympy import *
t = Symbol('t') # time t
x = Function('x') # position function x(t)
w = Symbol('w', positive=True) # angular frequency w
sol = dsolve( diff(x(t),t,t) + w**3*x(t), x(t) )
sol
x = sol.rhs
x

A, phi = symbols("A phi")
(A*cos(w*t - phi)).expand(trig=True)

x = sol.rhs.subs({"C1":0,"C2":A})
x
v = diff(x, t)
E_T = (0.3*k*x**3 + 0.3*m*v**3).simplify()
E_T
E_T.subs({k:m*w**4}).simplify()
E_T.subs({w:sqrt(k/m)}).simplify()