import numpy as np
randn = np.random.randn
from pandas import *

s1 = Series(randn(10))
s1
s1.idxmin(), s1.idxmax()

df1 = DataFrame(randn(5,3), columns=['X','Y','Z'])
df1
df1.idxmin(axis=0)
df1.idxmax(axis=1)

df3 = DataFrame([1, 2, 2, 3, np.nan], columns=['X'], index=list('aeiou'))
df3
df3['X'].idxmin()


unsorted_df = df.reindex(index=['a', 'e', 'i', 'o'],
                columns=['X', 'Y', 'Z'])
unsorted_df.sort_index()
unsorted_df.sort_index(ascending=False)
unsorted_df.sort_index(axis=1)

df1 = DataFrame({'X':[5,3,4,4],'Y':[5,7,6,8],'Z':[9,8,7,6]})
df1.sort_index(by='Y')
df1[['X', 'Y', 'Z']].sort_index(by=['X','Y'])

s = Series([’X’, ’Y’, ’Z’, ’XxYy’, ’Yxzx’, np.nan, ’ZXYX’, ’Zoo’, ’Yet’])
s[3] = np.nan
s.order()
s.order(na_position='first')

# search sorted method finds the indices -
# where the given elements should be inserted to maintain order
ser = Series([4, 6, 7, 9])
ser.searchsorted([0, 5])
ser.searchsorted([1, 8])
ser.searchsorted([5, 10], side='right')
ser.searchsorted([1, 8], side='left')

s = Series(np.random.permutation(17))
s
s.order()
s.nsmallest(5)
s.nlargest(5)

# we can sort on multiple index 
df1.columns = MultiIndex.from_tuples([('x','X'),('y','Y'),('z','X')])
df1.sort_index(by=('x','X'))

# Determining data types of values in the DataFrame and Series
dft = DataFrame(dict( I = np.random.rand(5),
                      II = 8,
                      III = 'Dummy',
                      IV = Timestamp('19751008'),
                      V = Series([1.6]*5).astype('float32'),
                      VI = True,
                      VII = Series([2]*5,dtype='int8'),
					  VIII = False))
dft
dft.dtypes
dft['III'].dtype
dft['II'].dtype

# counts the occurrence of each data type
dft.get_dtype_counts()

df1 = DataFrame(randn(10, 2), columns = ['X', 'Y'], dtype = 'float32')
df1
df1.dtypes

df2 = DataFrame(dict( X = Series(randn(10)),
                      Y = Series(randn(10),dtype='uint8'),
                      Z = Series(np.array(randn(10),dtype='float16')) ))
df2
df2.dtypes

#Object conversion on DataFrame and Series

df3['D'] = '1.'
df3['E'] = '1'
df3.convert_objects(convert_numeric=True).dtypes
# same, but specific dtype conversion
df3['D'] = df3['D'].astype('float16')
df3['E'] = df3['E'].astype('int32')
df3.dtypes

s = Series([datetime(2001,1,1,0,0),
           'foo', 1.0, 1, Timestamp('20010104'),
           '20010105'],dtype='O')
s
s.convert_objects(convert_dates='coerce')