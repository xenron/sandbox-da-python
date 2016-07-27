cimport numpy
import numpy

def array_sum(numpy.ndarray[double, ndim = 1] a):
    cdef double sum
    cdef int i
    sum = 0
    for i in range(a.shape[0]):
        sum += a[i]
    return sum

