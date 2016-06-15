# -*- coding: utf-8 -*-
import pygal

#create a new bar chart.
bar = pygal.HorizontalBar()
bar.title = 'Searches for term: sleep in April'
bar.add('Searches', [81, 88, 88, 100])
bar.render_to_file('bar_chart.svg')
