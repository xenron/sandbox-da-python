# -*- coding: utf-8 -*-
import pygal

param_line_chart = pygal.Line(interpolate='cubic', label_font_size=20, x_label_rotation=50)
param_line_chart.title = 'Parameter Line Chart'
param_line_chart.x_title='Data-Sets (X Axis)'
param_line_chart.y_title='Values (Y Axis)'

param_line_chart.x_labels = map(str, ["Data Object 1", "Data Object 2", "Data Object 3", "Data Object 4", "Data Object 5", "Data Object 6"])

param_line_chart.add('Data-Set 1', [8, 16, 24, 32, 48, 56]) 
param_line_chart.add('Data-Set 2', [2, 4, 6, 8, 10, 12]) 
param_line_chart.add('Data-Set 3', [1, 3, 5, 7, 9, 12]) 

param_line_chart.render_to_file('lineparam.svg')
