#!/usr/bin/env python

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import scipy.signal
import matplotlib.pyplot
import scipy.fftpack
from matplotlib.dates import  DateFormatter, DayLocator, MonthLocator


today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo("QQQ", start, today)
quotes = numpy.array(quotes)

dates = quotes.T[0]
qqq = quotes.T[4]


y = scipy.signal.detrend(qqq)


alldays = DayLocator()              
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(211)

ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)

amps = numpy.abs(scipy.fftpack.fftshift(scipy.fftpack.rfft(y)))
amps[amps < 0.1 * amps.max()] = 0

matplotlib.pyplot.plot(dates, y, 'o', label="detrended")
matplotlib.pyplot.plot(dates, -scipy.fftpack.irfft(scipy.fftpack.ifftshift(amps)), label="filtered")
fig.autofmt_xdate()
matplotlib.pyplot.legend()

ax2 = fig.add_subplot(212)
N = len(qqq)
matplotlib.pyplot.plot(numpy.linspace(-N/2, N/2, N), amps, label="transformed")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
