# -*- coding: utf-8 -*-
import pygal


pie_chart = pygal.Pie()
pie_chart.title = 'Total top tablet sales in 2013 (in %)'
pie_chart.add('iPad & iPad mini', [19.7, 21.3])
pie_chart.add('Surface 2 (& Pro 2)', [24.5, 36.3])
pie_chart.add('Nexus 7', 17.5)

pie_chart.render_to_file('pie_chart.svg')
