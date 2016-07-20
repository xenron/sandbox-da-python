import multiprocessing as mpcs
import random
import string

def calc_square(n):
	return n**2

pool_processes = mpcs.Pool(processes=5)

results = [pool_processes.apply(calc_square, args=(i,)) for i in range(1,10)]
print(results)

pool_processes = mpcs.Pool(processes=5)
results = pool_processes.map(calc_square, range(1,10))
print(results)