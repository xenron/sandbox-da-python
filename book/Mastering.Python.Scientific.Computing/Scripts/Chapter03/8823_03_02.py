import math
import random

def	next_poisson(lambdaValue):
	elambda = math.exp(-1*lambdaValue)
	product = 1
	count = 0
	while (product >= elambda):
		product *= random.random()
		result = count
		count+=1
	return result
for x in range(1, 9):
	print nextPoisson(8)
