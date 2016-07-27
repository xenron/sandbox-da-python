#!/usr/bin/env python

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import matplotlib.pyplot
import scipy.fftpack
import scipy.signal
from matplotlib.dates import  DateFormatter, DayLocator, MonthLocator
import scipy.optimize


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
amps[amps < amps.max()] = 0

def residuals(p, y, x):
   A,k,theta,b = p
   err = y-A * numpy.sin(2* numpy.pi* k * x + theta) + b

   return err

filtered = -scipy.fftpack.irfft(scipy.fftpack.ifftshift(amps))
N = len(qqq)
f = numpy.linspace(-N/2, N/2, N)
p0 = [filtered.max(), f[amps.argmax()]/(2*N), 0, 0]
print "P0", p0

plsq = scipy.optimize.leastsq(residuals, p0, args=(filtered, dates))
p = plsq[0]
print "P", p
matplotlib.pyplot.plot(dates, y, 'o', label="detrended")
matplotlib.pyplot.plot(dates, filtered, label="filtered")
matplotlib.pyplot.plot(dates, p[0] * numpy.sin(2 * numpy.pi * dates * p[1] + p[2]) + p[3], '^', label="fit")
fig.autofmt_xdate()
matplotlib.pyplot.legend()

ax2 = fig.add_subplot(212)
matplotlib.pyplot.plot(f, amps, label="transformed")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
