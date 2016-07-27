s1_n = 1/n
s2_n = 1/factorial(n)
summation(s1_n, [n, 1, oo])
summation(s2_n, [n, 0, oo])
import math
def s2_nf(n):
	return 1.0/math.factorial(n)

sum( [s2_nf(n) for n in range(0,10)] )
E.evalf()

exponential_xn = x**n/factorial(n)
summation( exponential_xn.subs({x:5}), [x, 0, oo] ).evalf()
exp(5).evalf()
summation( exponential_xn.subs({x:5}), [x, 0, oo])

import math # redo using only python
def exponential_xnf(x,n):
	return x**n/math.factorial(n)
sum( [exponential_xnf(5.0,i) for i in range(0,35)] )

series( sin(x), x, 0, 8)
series( cos(x), x, 0, 8)
series( sinh(x), x, 0, 8)
series( cosh(x), x, 0, 8)
series(ln(x), x, 1, 6) # Taylor series of ln(x) at x=1
series(ln(x+1), x, 0, 6) # Maclaurin series of ln(x+1)