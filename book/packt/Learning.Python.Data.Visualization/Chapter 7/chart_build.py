import pygal
from pygal import Config

'''Creating our own class with values to pass in as parameters to our chart.'''
class ConfigChart(Config):
    show_legend = True
    human_readable = True
    fill = True
    '''explicit_size sets a fixed size to our width height properties.'''
    explicit_size = True 
    width = 860
    height = 640
    title= 'Posts per month on Packtpub.com'
    y_label = 'Posts'
    x_label = 'Month'
    y_title = 'Posts'
    x_title = 'Month'
    show_y_labels = True
    show_x_labels = True
    stroke = False
    tooltip_font_size = 42
    title_font_size = 24
    '''Always include an error message for any dynamic data.'''
    no_data_text = 'Unable to load data'

'''Generate chart based on imported array, (with 2 values)'''
def generate_chart(dataarr):

    '''Initialize the chart with our ConfigChart class.'''
    mychart = pygal.Bar(ConfigChart())

    '''Add data to the chart for May and June.'''
    mychart.add('May', dataarr[0])
    mychart.add('June', dataarr[1])

    '''Launch our web browser with our SVG, (we can also render to file as well)'''
    mychart.render_in_browser()