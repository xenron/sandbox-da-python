from scipy.integrate import odeint
import matplotlib.pyplot as plt
def derivative(x,time): 
	a = -2.0
	b = -0.1
	return array([ x[1], a*x[0]+b*x[1] ])

time = linspace(0.0,10.0,1000)

xinitialize = array([0.0005,0.2]) 
x = odeint(derivative,xinitialize,time)
plt.figure()
plt.plot(time,x[:,0]) 
plt.xlabel('t’)
plt.ylabel('x’)
plt.show()