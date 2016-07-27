integrate(x**3+1, x)
integrate(x*sin(x), x)
integrate(x+ln(x), x)

F = integrate(x**3+1, x)
F.subs({x:1}) - F.subs({x:0})

integrate(x**3-x**2+x, (x,0,1))		# definite Integrals 
integrate(sin(x)/x, (x,0,pi))		# definite Integrals 
integrate(sin(x)/x, (x,pi,2*pi))	# definite Integrals 
integrate(x*sin(x)/(x+1), (x,0,2*pi)) # definite Integrals 
