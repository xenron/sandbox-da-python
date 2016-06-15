# -*- coding: utf-8 -*-
import pygal

gauge_chart = pygal.Gauge()
gauge_chart.title = 'Speed of space shuttle during takeoff'
gauge_chart.x_labels = ['Pre-takeoff', '5 min', ' 10 min', '15 min', '20 min']
gauge_chart.add('Pre-takeoff', 0)
gauge_chart.add('5 min', 96)
gauge_chart.add('10 min', 167)
gauge_chart.add('15 min', 249)
gauge_chart.add('20 min', 339)

gauge_chart.render_to_file('gauge_chart.svg')
