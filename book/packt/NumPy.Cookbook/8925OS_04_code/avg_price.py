import urllib2
import re
import time
import sys
import numpy

prices = numpy.array([])

for i in xrange(3):
   req = urllib2.Request('http://finance.google.com/finance/info?client=ig&q=' + sys.argv[1])
   req.add_header('User-agent', 'Mozilla/5.0')
   response = urllib2.urlopen(req)
   page = response.read()
   m = re.search('l_cur" : "(.*)"', page)
   prices = numpy.append(prices, float(m.group(1)))
   avg = prices.mean()
   sigma = prices.std()
 
   devFactor = float(sys.argv[2])
   bottom = avg - devFactor * sigma
   top = avg + devFactor * sigma
   timestr = time.strftime("%H:%M:%S", time.gmtime())
 
   print timestr, "Average", avg, "-Std", bottom, "+Std", top 
   time.sleep(60)
