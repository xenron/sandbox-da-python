# -*- coding: utf-8 -*-
import pygal


pie_chart = pygal.Pie()
pie_chart.title = 'Total top tablet sales in 2013 (in %)'
pie_chart.add('iPad & iPad mini', 49.7)
pie_chart.add('Surface Pro 2', 36.3)
pie_chart.add('Surface 2', 24.5)
pie_chart.add('Nexus 7', 17.5)

pie_chart.render_to_file('pie_chart.svg')
