# -*- coding: utf-8 -*-
import pygal

xy_chart = pygal.XY()
xy_chart.add('Value 1',  [(-50, -30), (100, 45)])
xy_chart.add('Value 2',  [(-2, -14), (370, 444)])
xy_chart.render_to_file("xy_chart.svg")
