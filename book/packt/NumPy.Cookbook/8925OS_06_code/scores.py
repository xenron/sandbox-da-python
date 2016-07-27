import numpy
from matplotlib.finance import quotes_historical_yahoo
from datetime import date

# DJIA stock with div yield > 4 %
tickers = ['MRK', 'T', 'VZ']

def get_close(ticker):
   today = date.today()
   start = (today.year - 1, today.month, today.day)

   quotes = quotes_historical_yahoo(ticker, start, today)

   return numpy.array([q[4] for q in quotes])


weights = numpy.recarray((len(tickers),), dtype=[('symbol', numpy.str_, 16), 
   ('stdscore', float), ('mean', float), ('score', float)])

for i in xrange(len(tickers)):
   close = get_close(tickers[i])
   logrets = numpy.diff(numpy.log(close))
   weights[i]['symbol'] = tickers[i]
   weights[i]['mean'] = logrets.mean()
   weights[i]['stdscore'] = 1/logrets.std()
   weights[i]['score'] = 0

for key in ['mean', 'stdscore']:
   wsum = weights[key].sum()
   weights[key] = weights[key]/wsum

weights['score'] = (weights['stdscore'] + weights['mean'])/2
weights['score'].sort()

for record in weights:
   print "%s,mean=%.4f,stdscore=%.4f,score=%.4f" % (record['symbol'], record['mean'], record['stdscore'], record['score'])
