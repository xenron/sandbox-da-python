import numpy as np
randn = np.random.randn
from pandas import *

s = Series(randn(10), index=[’I’, ’II’, ’III’, ’IV’, ’V’, ’VI’, ’VII’, ’VIII’, ’IX’, ’X’ ])
s
s.index

Series(randn(10))

d = {’a’ : 0., ’e’ : 1., ’i’ : 2.}
Series(d)
Series(d, index=[’e’, ’i’, ’o’, ’a’])

#Series creation using scalar value 
Series(6., index=[’a’, ’e’, ’i’, ’o’, ’u’, ’y’])


Series([10, 20, 30, 40], index=['a', 'e', 'i', 'o'])


Series({'a': 10, 'e': 20, 'i': 30})

s.get('VI')

# name attribute can be specified
s = Series(np.random.randn(5), name='RansomSeries')