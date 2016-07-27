# -*- coding: utf-8 -*-
import pygal
radar_chart = pygal.Radar()
radar_chart.title = 'Product Budget Figures'
radar_chart.x_labels = ['Sales', 'Marketing', 'Development', 'Customer support', 'Information Technology', 'Administration']
radar_chart.add('Estimate', [40, 20, 100, 20, 30, 20, 10])
radar_chart.add('Actual Spending', [70, 50, 40, 10, 17, 8, 10])
radar_chart.render_to_file('radar_chart.svg')