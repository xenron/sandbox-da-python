import numpy as np
randn = np.random.randn
from pandas import *

#From Dict of Series/ dicts
d = {'first' : Series([10., 20., 30.], index=['I', 'II', 'III']),
     'second' : Series([10., 20., 30., 40.], index=['I', 'II', 'III', 'IV'])}
DataFrame(d, index=['IV', 'II', 'I'])

DataFrame(d, index=['IV', 'II', 'I'], columns=['second', 'third'])
df = DataFrame(d)
df
df.index
df.columns

#dict of ndarray/list
d = {'one' : [10., 20., 30., 40.],
      'two' : [40., 30., 20., 10.]}
DataFrame(d)
DataFrame(d, index=['I', 'II', 'III', 'IV'])

# Array of Structure/ record
data = np.zeros((2,),dtype=[('I', 'i4'),('II', 'f4'),('III', 'a10')])
data[:] = [(10,20.,'Very'),(20,30.,"Good")]

DataFrame(data)
DataFrame(data, index=['first', 'second'])
DataFrame(data, columns=['III', 'I', 'II'])