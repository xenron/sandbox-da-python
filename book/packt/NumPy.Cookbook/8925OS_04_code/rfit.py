from numpy import array, rec
from numpy.random import normal as nprandom
from rpy2.robjects import numpy2ri, r

foo = array(range(10))
bar = foo + nprandom(0,1,10)

d = rec.fromarrays([foo, bar], names=('foo','bar'))
print d
fit = r.lm('bar ~ foo', data=d)
print fit.rx2('coefficients')
