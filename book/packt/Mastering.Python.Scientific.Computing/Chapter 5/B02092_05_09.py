import numpy as np
from nympy import linalg as LA
x2d = np.array((	(100,200,300), 
					(111,222,333), 
					(129,461,795) ))
w, v = LA.eig(x2d)
LA.norm(x2d)
LA.det(x2d)
LA.inv(x2d)
a = np.array([[2,3], [3,4]])
b = np.array([4,5])
x = np.linalg.solve(a, b)
print x
np.allclose(np.dot(a, x), b)