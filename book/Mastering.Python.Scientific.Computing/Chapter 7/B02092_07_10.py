import numpy as np
randn = np.random.randn
from pandas import *

# Panel creation from a three diemsional array of random numbers with axis labels.
workpanel = Panel(randn(2, 3, 5), items=[’FirstItem’, ’SecondItem’],
     major_axis=date_range(’1/1/2010’, periods=3),
     minor_axis=[’A’, ’B’, ’C’, ’D’, ’E’])
workpanel

# Panel creation from Dict of DataFrame
data = {’FirstItem’ : DataFrame(randn(4, 3)),
       ’SecondItem’ : DataFrame(randn(4, 2))}
Panel(data)

# orient=minor indicates to use the DataFrame's column as items
Panel.from_dict(data, orient=’minor’)

df = DataFrame({’x’: [’one’, ’two’, ’three’, ’four’],’y’: np.random.randn(4)})
df

data = {’firstitem’: df, ’seconditem’: df}
panel = Panel.from_dict(data, orient=’minor’)
panel[’x’]
panel[’y’]
panel[’y’].dtypes

workpanel[’FirstItem’]

# To rearrange the panel we can use transpose method.
workpanel.transpose(2, 0, 1)

#Select a particular Item
workpanel[’FirstItem’]

# Fetch a slice at given major_axis label
workpanel.major_xs(wp.major_axis[1])

workpanel.minor_axis
# Fetch a slice at given minor_axis label
workpanel.minor_xs(’D’)

# The dimensionality can be changes using squeeze method.
workpanel.reindex(items=[’FirstItem’]).squeeze()
workpanel.reindex(items=[’FirstItem’],minor=[’B’]).squeeze()


forconversionpanel = Panel(randn(2, 4, 5), items=[’FirstItem’, ’SecondItem’],
     major_axis=date_range(’1/1/2010’, periods=4),
     minor_axis=[’A’, ’B’, ’C’, ’D’, ’E’])
forconversionpanel.to_frame()