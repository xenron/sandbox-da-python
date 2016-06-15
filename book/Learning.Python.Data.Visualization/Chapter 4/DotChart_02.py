 # -*- coding: utf-8 -*-
import pygal

dot_chart = pygal.Dot(x_label_rotation=45)
dot_chart.title = 'Cost of Whole Milk in early 2014'
dot_chart.x_labels = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June']
dot_chart.add('US Dollars', [2.08, 3.14, 3.89, 3.91, 3.94, 3.98])
dot_chart.add('Pound Sterling', [2.78, 3.84, 1.69, 4.71, 4.84, 4.92])


dot_chart.render_to_file('dot_chart.svg')
