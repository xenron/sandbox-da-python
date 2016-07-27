# -*- coding: utf-8 -*-
import pygal

worldmap_chart = pygal.Worldmap()
worldmap_chart.title = 'Highlighting China and the United States'
worldmap_chart.add('China', ['cn'])
worldmap_chart.add('United States', ['us'])

#Render file.
worldmap_chart.render_to_file('world_map.svg')
