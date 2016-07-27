# -*- coding: utf-8 -*-
import pygal, time
from datetime import datetime

#Set pre-defined arrival dates for compare.
arrival1 = datetime.now()
time.sleep(277)
arrival2 = datetime.now()

delta = arrival2 - arrival1
result = str(delta.seconds) + ' seconds'


Date_Y = pygal.DateY(x_label_rotation=25)
Date_Y.title = "Flights and amount of passengers arriving from St. Louis."
Date_Y.add("Arrival", [
    (datetime(2014, 1, 5), 42), 
    (datetime(2014, 1, 14), 123),
    (datetime(2014, 2, 2), 97),
    (datetime(2014, 3, 22), 164)
])
Date_Y.add("Arrivals today (time between flights %s)" % result, [
(arrival1, 14), 
(arrival2, 47)
])

Date_Y.render_to_file('datey_chart.svg')
