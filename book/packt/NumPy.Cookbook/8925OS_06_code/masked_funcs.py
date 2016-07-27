import numpy
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import sys
import matplotlib.pyplot

def get_close(ticker):
   today = date.today()
   start = (today.year - 1, today.month, today.day)

   quotes = quotes_historical_yahoo(ticker, start, today)

   return numpy.array([q[4] for q in quotes])


close = get_close(sys.argv[1])

triples = numpy.arange(0, len(close), 3)
print "Triples", triples[:10], "..."

signs = numpy.ones(len(close))
print "Signs", signs[:10], "..."

signs[triples] = -1
print "Signs", signs[:10], "..."

ma_log = numpy.ma.log(close * signs)
print "Masked logs", ma_log[:10], "..."

dev = close.std()
avg = close.mean()
inside = numpy.ma.masked_outside(close, avg - dev, avg + dev)
print "Inside", inside[:10], "..."

matplotlib.pyplot.subplot(311)
matplotlib.pyplot.title("Original")
matplotlib.pyplot.plot(close)

matplotlib.pyplot.subplot(312)
matplotlib.pyplot.title("Log Masked")
matplotlib.pyplot.plot(numpy.exp(ma_log))

matplotlib.pyplot.subplot(313)
matplotlib.pyplot.title("Not Extreme")
matplotlib.pyplot.plot(inside)

matplotlib.pyplot.show()

#Triples [ 0  3  6  9 12 15 18 21 24 27] ...
#Signs [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.] ...
#Signs [-1.  1.  1. -1.  1.  1. -1.  1.  1. -1.] ...
#Masked logs [-- 5.93655586575 5.95094223368 -- 5.97468290742 5.97510711452 --
# 6.01674381162 5.97889061623 --] ...
#Inside [-- -- -- -- -- -- 409.429675172 410.240597855 -- --] ...
