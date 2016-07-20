from sympy import *
xi = 20 # initial position
vi = 10 # initial velocity
a = 5 # acceleration (constant during motion)
x = xi + integrate( vi+integrate(a,(t,0,t)), (t,0,t) )
x
x.subs({t:3}).n() # x(3) in [m]
diff(x,t).subs({t:3}).n() # v(3) in [m/s]

t, vi, xi, k = symbols('t vi xi k')
a = sqrt(k*t)
x = xi + integrate( vi+integrate(a,(t,0,t)), (t, 0,t) )
x

x, y = symbols('x y')
m, g, k, h = symbols('m g k h')
F_g = -m*g # Force of gravity on mass m
U_g = - integrate( F_g, (y,0,h) )
U_g
F_s = -k*x # Spring force for displacement x
U_s = - integrate( F_s, (x,0,x) )
U_s