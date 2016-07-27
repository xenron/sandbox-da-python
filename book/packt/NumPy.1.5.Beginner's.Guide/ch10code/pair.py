#!/usr/bin/env python

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import scipy.stats
import scikits.statsmodels.stattools
import matplotlib.pyplot


def get_close(symbol):
   today = date.today()
   start = (today.year - 1, today.month, today.day)

   quotes = quotes_historical_yahoo(symbol, start, today)
   quotes = numpy.array(quotes)

   return quotes.T[4]

spy =  numpy.diff(numpy.log(get_close("SPY")))
dia =  numpy.diff(numpy.log(get_close("DIA")))

print "Means comparison", scipy.stats.ttest_ind(spy, dia)
print "Kolmogorov smirnov test", scipy.stats.ks_2samp(spy, dia)

print "Jarque Bera test", scikits.statsmodels.stattools.jarque_bera(spy - dia)[1]

matplotlib.pyplot.hist(spy, histtype="step", lw=1, label="SPY")
matplotlib.pyplot.hist(dia, histtype="step", lw=2, label="DIA") 
matplotlib.pyplot.hist(spy - dia, histtype="step", lw=3, label="Delta")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
