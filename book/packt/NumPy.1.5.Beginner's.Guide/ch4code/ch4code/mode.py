#!/usr/bin/python

import numpy

print "Unique", numpy.unique(numpy.array([2, 2]))

bhp = numpy.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)

bhp_returns = numpy.diff(bhp) / bhp[ : -1]
print "BHP returns", bhp_returns

print "Total number", len(bhp_returns), "Unique number", len(numpy.unique(bhp_returns))

nbins = numpy.sqrt(len(bhp_returns))
N, bins = numpy.histogram(bhp_returns, bins=nbins)
print "Counts", N, "Bins", bins

index_max = N.argmax()
print "mode", bins[index_max]

bhp_promilles = (bhp_returns * 1000).astype(int)
sorted = numpy.sort(bhp_promilles)
print "Sorted", sorted

diffed = numpy.diff(sorted)

#values changed
indices = numpy.where(diffed > 0)
print "Indices where values changed", indices

# number of repeats
repeats = numpy.diff(indices)
print "Repeats", repeats

most_repeats_index = numpy.argmax(repeats)
print "Most repeats index", most_repeats_index

index = numpy.ravel(indices)[most_repeats_index + 1]
print "Index", index

print "Mode", sorted[index]
