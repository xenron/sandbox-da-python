s1_n = 1/n
s2_n = 1/factorial(n)
s1_n.subs({n:5})
[ s1_n.subs({n:index1}) for index1 in range(0,8) ]
[ s2_n.subs({n:index1}) for index1 in range(0,8) ]
limit(s1_n, n, oo)
limit(s2_n, n, oo)
