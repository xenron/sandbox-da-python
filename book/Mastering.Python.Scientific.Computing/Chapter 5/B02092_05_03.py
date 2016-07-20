import numpy as np
x = np.array([1,12, 25, 8, 15, 35, 50, 7, 2, 10])
x2d = np.array((	(100,200,300), 
					(111,222,333), 
					(123,456,789),
					(125,457,791),
					(127,459,793),
					(129,461,795) ))
for i in x:
	print i

for row in x2d:
	print row