import numpy as np
np.random.permutation(10)
np.random.randint(20,50, size=10)
np.random.random_sample(10)
np.random.chisquare(5,10) # degree of freedom, size

a, m = 4., 2. # shape and mode
s = np.random.pareto(a, 10) + m

s = np.random.standard_normal(20)

mu, sigma = 4., 2. # mean and standard deviation
s = np.random.lognormal(mu, sigma, 10)



