from pandas import *
randn = np.random.randn
import matplotlib.pyplot as plt
x1 = np.array( ((1,2,3), (1,4,6), (2,4,8)) )
df = DataFrame(x1, index=[’I’, ’II’, ’III’], columns=['A', 'B', 'C']) 
df = df.cumsum()

df.plot(kind='pie', subplots=True)
plt.figure()
plt.show()