# -*- coding: utf-8 -*-
import pygal

tablet1 = 'iPad & iPad mini', 49.7
tablet2 = 'Surface Pro 2', 36.3
tablet3 = 'Surface 2', 24.5
tablet4 = 'Nexus 7', 17.5

def createChart():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Total top tablet sales in 2013 (in %)' 
    pie_chart.add(tablet1[0], tablet1[1])
    pie_chart.add(tablet2[0], tablet2[1])
    pie_chart.add(tablet3[0], tablet3[1])
    pie_chart.add(tablet4[0], tablet4[1])
    
    pie_chart.render_to_file('pie_chart.svg')
    return pie_chart
