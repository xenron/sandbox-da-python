from sympy.physics.vector import vlatex, ReferenceFrame, dynamicsymbols
N = ReferenceFrame('N')
q1, q2 = dynamicsymbols('q1 q2')
q1d, q2d = dynamicsymbols('q1 q2', 1)
q1dd, q2dd = dynamicsymbols('q1 q2', 2)
vlatex(N.x + N.y)
vlatex(q1 + q2)
vlatex(q1d)
vlatex(q1 * q2d)
vlatex(q1dd * q1 / q1d)


from sympy.physics.vector import vprint, dynamicsymbols
u1 = dynamicsymbols('u1')
print(u1)
vprint(u1)