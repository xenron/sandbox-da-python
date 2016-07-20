from sympy import *
A = Matrix( [[1, 2, 3, 4],
			 [5, 6, 7, 8],
			 [ 9, 10, 11, 12],
			 [ 13, 14, 15, 16]] )
A.row_del(3)
A.col_del(3)

A.row_join(B)

A[0,1] # display row 0, col 1 of A

A[0:2,0:3] # top-left submatrix(2x3)

B = Matrix ([[1, 2, 3],
			 [5, 6, 7],
			 [ 9, 10, 11]] )

A.row_join(B)
B.col_join(B)
A + B
A - B
A * B
A **2 
eye(3) # 3x3 identity matrix
zeros((3, 3)) # 3x3 matrix with all elements Zeros
ones((3, 3)) # 3x3 matrix with all elements Ones

A.transpose() # It is same as A.T

A.rref()

A.nullspace() # N(A)

M = Matrix( [[1, 2, 3],
		[4, 5, 6],
		[7, 8, 10]] )

M.det()