# -*- coding: utf-8 -*-
import pygal

#create a new line chart.
line = pygal.Line() 
line.title = 'Website hits in the past 2 years' #set chart title
line.x_labels = map(str, range(2012, 2014)) #set the x-axis labels.
line.add('Page views', [None, 0, 12, 32, 72, 148]) #set values.
line.render_to_file('linechart.svg') #set filename.
