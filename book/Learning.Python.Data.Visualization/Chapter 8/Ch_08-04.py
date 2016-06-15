#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

'''import Plotly, and the main plotly object as a variable.'''
import plotly;
import plotly.plotly as py

'''import all chart types.'''
from plotly.graph_objs import *

'''Set the username, APIKey, and streaming IDs as given on https://plot.ly/python/getting-started/'''

plotly.tools.set_credentials_file(username='[username]', api_key='[apikey]', stream_ids=['[streamingkey1]', '[streamingkey2]'])

'''Create a data-set for a scatter plot.'''
trace0 = Scatter(
    #Create an array for each value.
    x=[27984, 9789],
    y=[34, 27],
    text=['Formula 1 Fans', 'Nascar Fans'],
    name='European automotive fans',
    mode='markers',
    marker=Marker(
        line=Line(
            color='rgb(124, 78, 42)',
            width=0
        ),
        size=48,
        color='rgb(124, 78, 42)'
    )
)

trace1 = Scatter(
    #Create an array for each value.
    x=[10117, 340159],
    y=[38, 31],
    text=['Formula 1 Fans', 'Nascar Fans'],
    name='North America automotive fans',
    mode='markers',
    marker=Marker(
        line=Line(
            color='rgb(114, 124, 195)',
            width=0
        ),
        size=48,        
        color='rgb(114, 124, 195)'
    )
)

'''Set chart\'s titles, labels, and values.'''
layout = Layout(
    title='Fan comparisons of automotive sports in the United States and Europe',
    xaxis=XAxis(
        title='Amount of fans',
        showgrid=True,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Average age of fans sampled',
        showline=True
    )
)

'''Assign the data to an array typed variable to hold data.'''
data = Data([trace0, trace1])

'''Add full chart labels to the chart.'''
fig = Figure(data=data, layout=layout)

'''Create a URL with the data loaded via the API, pass the data to the figure which is passed here, and then open a web browser to the chart on success.'''
unique_url = py.plot(fig, filename = 'line-style')
