#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from matplotlib import pyplot

#Create a range from 0 - 541
X = range(0, 541)

#Set the values for Y by iterating thru X's range.
Y = [i*i for i in X]

#Assign values to the graph.
pyplot.plot(X, Y, '-')

#Set chart's labels and title
pyplot.title('Plotting x*x')
pyplot.xlabel('X Axis')
pyplot.ylabel('Y Axis')

#Save the chart as a PNG to our project directory.
pyplot.savefig('Simple.png')

#Show the chart in the Python runtime viewer.
pyplot.show()