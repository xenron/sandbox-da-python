from sympy.physics.paulialgebra import Pauli, evaluate_pauli_product
from sympy.physics.matrices import mdft, mgamma, msigma, pat_matrix


mdft(4) # expression of discrete Fourier transform as a matrix multiplication
mgamma(2) # Dirac gamma matrix in the Dirac representation
msigma(2) #  Pauli matrix with (1,2,3)
pat_matrix(3, 1, 0, 0) #  computer Parallel Axis Theorem matrix to translate the inertia matrix a distance of dx, dy, dz for a body of mass m.
					   

evaluate_pauli_product(4*x*Pauli(3)*Pauli(2)) 