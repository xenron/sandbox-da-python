# -*- coding: utf-8 -*-
import pygal

funnel_chart = pygal.Funnel(x_label_rotation=40)
funnel_chart.title = 'Amount of thrust used in a space shuttle at takeoff (in lbs)'
funnel_chart.x_labels = ['Pre-takeoff', '5 min', ' 10 min', '15 min', '20 min']
funnel_chart.add('Main Engine', [7000000, 6115200, 5009600, 4347400, 2341211])
funnel_chart.add('Engine #1', [1285000, 1072000, 89000, 51600, 12960])
funnel_chart.add('Engine #3 & #4 (mid-size)', [99000, 61600, 21960, 17856, 11235])

funnel_chart.render_to_file('funnel_chart.svg')
