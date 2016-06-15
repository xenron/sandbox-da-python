# -*- coding: utf-8 -*-
import pygal

france_chart = pygal.FrenchMap_Departments()
france_chart.title = 'Sample departments'
france_chart.add('Data-set 1', ['17'])
france_chart.add('Data-set 2', ['27'])
france_chart.add('Data-set 3', ['38'])
france_chart.add('Data-set 4', ['42'])
france_chart.add('Data-set 5', ['19'])
france_chart.render_to_file('france_map.svg')
