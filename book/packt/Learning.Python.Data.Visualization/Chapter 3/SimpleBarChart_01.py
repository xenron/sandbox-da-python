# -*- coding: utf-8 -*-
import pygal

#create a new bar chart.
bar = pygal.Bar()
bar.title = 'Searches for term: sleep'
bar.x_labels = map(str, range(2011, 2015))
bar.add('Searches', [81, 88, 88, 100])
bar.render_to_file('bar_chart.svg')
