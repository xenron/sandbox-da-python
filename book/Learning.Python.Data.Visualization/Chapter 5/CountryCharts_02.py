# -*- coding: utf-8 -*-
import pygal

france_chart = pygal.FrenchMap_Regions()
france_chart.title = 'Sample Regions'
france_chart.add('Centre', ['24'])
france_chart.add('Lorraine', ['41'])
france_chart.add('Picardy', ['22'])
france_chart.add('Upper Normandy', ['23'])
france_chart.add('Corsica', ['94'])
france_chart.render_to_file('france_map.svg')
