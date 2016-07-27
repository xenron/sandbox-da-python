from sympy import limit, oo, symbols,exp, cos

oo+1
5000 < oo
1/oo

x , n = symbols ('x n')
limit( ((x**n - 1)/ (x - 1) ), x, 1)

limit( 1/x**2, x, 0)
limit( 1/x, x, 0, dir="-")

limit(cos(x)/x, x, 0)
limit(sin(x)**2/x, x, 0)
limit(exp(x)/x,x,oo)