from sympy import *
A = Matrix( [[1,2],
	[3,4]] )
A.inv()
A.inv()*A
A*A.inv()
A = Matrix( [[ 1, -2],
	 [-2, 3]] )
A.eigenvals() # same as solve( det(A-eye(2)*x), x)
A.eigenvects()
	
x = Symbol('x')
M = eye(3) * x
M.subs(x, 4)
y = Symbol('y')
M.subs(x, y)

M.inv()
M.inv("LU")	

A = Matrix([[1,2,1],[2,3,3],[1,3,2]])
Q, R = A.QRdecomposition()
Q

M = [Matrix([1,2,3]), Matrix([3,4,5]), Matrix([5,7,8])]
result1 = GramSchmidt(M)
result2 = GramSchmidt(M, True)
