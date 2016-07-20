import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh

np.random.seed(0)
X = np.random.random((75,75)) - 0.5
X = np.dot(X, X.T) 

evals_all, evecs_all = eigh(X)
evals_large, evecs_large = eigsh(X, 3, which=’LM’)
print evals_all[-3:]
print evals_large
print np.dot(evecs_large.T, evecs_all[:,-3:])