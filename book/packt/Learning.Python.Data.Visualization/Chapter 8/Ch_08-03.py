#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

'''import Plotly, and the main plotly object as a variable.'''
import plotly;
import plotly.plotly as py

'''import all chart types.'''
from plotly.graph_objs import *

'''Set the username, APIKey, and streaming IDs as given on https://plot.ly/python/getting-started/'''
plotly.tools.set_credentials_file(username='[username]', api_key='[apikey]', stream_ids=['[streamingkey1]', '[streamingkey2]'])

'''Create a data-set for a Plotly scatter plot.'''
trace0 = Scatter(
    x=[5, 10, 15, 20],
    y=[20, 40, 35, 16]
)

'''Assign the chart's data to an array typed variable (in this case trace0) to hold data.'''
data = Data([trace0])

'''Create a URL with the data loaded via the API, and open a web browser to the chart on success.'''
unique_url = py.plot(data, filename = 'basic-line')
