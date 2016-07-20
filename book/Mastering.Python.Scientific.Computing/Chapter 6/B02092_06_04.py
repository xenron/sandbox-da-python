from sympy import solve

solve (6*x**2 - 3*x - 30,x)

a, b, c = symbols('a b c')
solve( a*x**2 + b*x + c, x)
gen_sol = solve( a*x**2 + b*x + c, x)
[ gen_sol[0].subs({'a':6,'b':-3,'c':-30}),
gen_sol[1].subs({'a':6,'b':-3,'c':-30}) ]

 solve([2*x + 3*y - 3, x -2* y + 1], [x, y])