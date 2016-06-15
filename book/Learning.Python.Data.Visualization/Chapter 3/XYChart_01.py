# -*- coding: utf-8 -*-
import pygal

xy_chart = pygal.XY()
xy_chart.add('Value 1',  [(-50, -30), (100, 45)])
xy_chart.render_to_file("xy_chart.svg")
