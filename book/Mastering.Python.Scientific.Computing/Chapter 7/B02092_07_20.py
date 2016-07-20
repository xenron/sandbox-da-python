import numpy as np
randn = np.random.randn
from pandas import *

first_frame = DataFrame({'key': range(10), 
                           'left_value': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']})
second_frame = DataFrame({'key': range(2, 12), 
                           'right_value': ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']})
print first_frame
print second_frame

#Natural Join Operation 
print merge(left_frame, right_frame, on='key', how='inner') 
# Left, Right and Full Outer Join Operation
print merge(left_frame, right_frame, on='key', how='left')
print merge(left_frame, right_frame, on='key', how='right')
print merge(left_frame, right_frame, on='key', how='outer')


concat([left_frame, right_frame])
concat([left_frame, right_frame], axis=1)

headers = ['name', 'title', 'department', 'salary']
chicago_details = read_csv('c:\city-of-chicago-salaries.csv',
                      header=False,
                      names=headers,
                      converters={'salary': lambda x: float(x.replace('$', ''))})
print chicago_detail.head()

dept_group = chicago_details.groupby('department')
print dept_group

print dept_group.count().head(10) 

print dept_group.size().tail(10) 

print dept_group.sum()[10:17] 

print dept_group.mean()[10:17] 

print dept_group.median()[10:17] 
chicago_details.sort('salary', ascending=False, inplace=True)
