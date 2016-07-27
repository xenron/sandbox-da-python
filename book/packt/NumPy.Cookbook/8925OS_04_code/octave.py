import numpy
import scipy.io

a = numpy.arange(7)

scipy.io.savemat("a.mat", {"array": a})
