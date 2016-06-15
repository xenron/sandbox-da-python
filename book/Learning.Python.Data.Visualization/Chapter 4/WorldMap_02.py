# -*- coding: utf-8 -*-
import pygal

worldmap_chart = pygal.Worldmap()
worldmap_chart.title = 'United States Allies and China'
worldmap_chart.add('China', ['cn'])
worldmap_chart.add('U.S. Allies', ['al',
'be','bg','ca','hr','cz','dk','ee','ff','de','hu','is','it',
'lv','lt','lu','nl','no','pl','pt','ro','si','sk','tr','us','uk'])

#Render file.
worldmap_chart.render_to_file('world_map.svg')
