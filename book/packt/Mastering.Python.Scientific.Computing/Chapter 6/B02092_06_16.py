u = Matrix([ 1,2,3])
v = Matrix([-2,3,3])
u.dot(v)

acos(u.dot(v)/(u.norm()*v.norm())).evalf()
u.dot(v) == v.dot(u)
u = Matrix([2,3,4])
n = Matrix([2,2,3])
(u.dot(n) / n.norm()**2)*n  # projection of v in the n dir

w = (u.dot(n) / n.norm()**2)*n
v = u - (u.dot(n)/n.norm()**2)*n # same as u - w
u = Matrix([ 1,2,3])
v = Matrix([-2,3,3])
u.cross(v)
(u.cross(v).norm()/(u.norm()*v.norm())).n()

u1,u2,u3 = symbols('u1:4')
v1,v2,v3 = symbols('v1:4')
Matrix([u1,u2,u3]).cross(Matrix([v1,v2,v3]))
u.cross(v)
v.cross(u)