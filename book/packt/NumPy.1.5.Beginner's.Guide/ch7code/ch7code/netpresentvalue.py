#!/usr/bin/python

import numpy

cashflows = numpy.random.randint(100, size=5)
cashflows = numpy.insert(cashflows, 0, -100)
print "Cashflows", cashflows

print "Net present value", numpy.npv(0.03, cashflows)
