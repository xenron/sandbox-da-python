import pandas.io.data as web
import datetime
f1=web.DataReader("F", ’yahoo’, datetime.datetime(2010, 1, 1), datetime.datetime(2011, 12, 31))
f2=web.DataReader("F", ’google’, datetime.datetime(2010, 1, 1), datetime.datetime(2011, 12, 31))
f3=web.DataReader("GDP", "fred", datetime.datetime(2010, 1, 1), datetime.datetime(2011, 12, 31))
f1.ix[’2010-05-12’]

