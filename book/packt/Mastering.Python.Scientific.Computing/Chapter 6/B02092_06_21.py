from sympy.physics.hep.gamma_matrices import GammaMatrixHead
from sympy.physics.hep.gamma_matrices import GammaMatrix as GM
from sympy.tensor.tensor import tensor_indices, tensorhead
GMH = GammaMatrixHead()
index1 = tensor_indices('index1', G.LorentzIndex)
GMH(index1)

index1 = tensor_indices('index1', GammaMatrix.LorentzIndex)
GM(index1)

GammaMatrix.LorentzIndex.metric




p, q = tensorhead('p, q', [G.LorentzIndex], [[1]])
index0,index1,index2,index3,index4,index5 = tensor_indices('index0:6', G.LorentzIndex)
ps = p(index0)*GM(-index0)
qs = q(index0)*GM(-index0)
GM.gamma_trace(GM(index0)*GM(index1))
GM.gamma_trace(ps*ps) - 4*p(index0)*p(-index0)
GM.gamma_trace(ps*qs + ps*ps) - 4*p(index0)*p(-index0) - 4*p(index0)*q(-index0)

p, q = tensorhead('p, q', [GM.LorentzIndex], [[1]])
index0,index1,index2,index3,index4,index5 = tensor_indices('index0:6', G.LorentzIndex)
ps = p(index0)*G(-index0)
qs = q(index0)*G(-index0)
GM.simplify_gpgp(ps*qs*qs)

index0,index1,index2,index3,index4,index5 = tensor_indices('index0:6', GammaMatrix.LorentzIndex)
spinorindex0,spinorindex1,spinorindex2,spinorindex3,spinorindex4,spinorindex5,spinorindex6,spinorindex7 = tensor_indices('spinorindex0:8', DiracSpinorIndex)
GM = GammaMatrix
t = GM(index1,spinorindex1,-spinorindex2)*GM(index4,spinorindex7,-spinorindex6)*GM(index2,spinorindex2,-spinorindex3)*GM(index3,spinorindex4,-spinorindex5)*GM(index5,spinorindex6,-spinorindex7)
GM.simplify_lines(t)