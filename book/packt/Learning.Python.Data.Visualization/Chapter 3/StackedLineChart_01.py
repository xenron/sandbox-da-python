# -*- coding: utf-8 -*-
import pygal

#create a new stacked line chart.
line = pygal.StackedLine(fill=True)
line.title = 'Web hits in the past 2 years' #set chart title
line.x_labels = map(str, range(2012, 2014)) #set the x-axis labels.
line.add('Site A', [None, 0, 12, 32, 72, 148]) #set values.
line.add('Site B', [2, 16, 12, 87, 91, 342]) #set values.
line.add('Site C', [42, 55, 84, 88, 90, 171]) #set values.
line.render_to_file('linechart.svg') #set filename.
