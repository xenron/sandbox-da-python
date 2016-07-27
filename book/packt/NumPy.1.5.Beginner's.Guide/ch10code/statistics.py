#!/usr/bin/python

import scipy.stats
import matplotlib.pyplot

generated = scipy.stats.norm.rvs(size=900)
print "Mean", "Std", scipy.stats.norm.fit(generated)
print "Skewtest", "pvalue", scipy.stats.skewtest(generated)
print "Kurtosistest", "pvalue", scipy.stats.kurtosistest(generated)
print "Normaltest", "pvalue", scipy.stats.normaltest(generated)
print "95 percentile", scipy.stats.scoreatpercentile(generated, 95)
print "Percentile at 1", scipy.stats.percentileofscore(generated, 1)
matplotlib.pyplot.hist(generated)
matplotlib.pyplot.show()
