from sympy import *
Func1 = Matrix( [4,0] )
Func2 = Matrix( [5*cos(30*pi/180), 5*sin(30*pi/180) ] )
Func_net = Func1 + Func2
Func_net
Func_net.evalf()

Func_net.norm().evalf()
(atan2( Func_net[1],Func_net[0] )*180/pi).n()

t, a, vi, xi = symbols('t vi xi a')
v = vi + integrate(a, (t, 0,t) )
v
x = xi + integrate(v, (t, 0,t) )
x

(v*v).expand()
((v*v).expand() - 2*a*x).simplify()