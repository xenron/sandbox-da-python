import numpy as np
from IPython.parallel import Client
ndim = 5
mat1 = np.random.randn(ndim, ndim)
mat2 = np.random.randn(ndim, ndim)
mat3 = np.dot(mat1,mat2)
clnt = Client(profile='testprofile')
clnt.ids
dvw = clnt[:]
dvw.execute('import numpy as np', block=True)
dvw.push(dict(a=mat1, b=mat2), block=True)
rslt = dvw.execute('mat3 = np.dot(a,b); print mat3', block=True)
rslt.display_outputs()
dot_product = dvw.pull('mat3', block=True)
print dot_product
np.allclose(mat3, dot_product[0])
np.allclose(dot_product[0], dot_product[1])
np.allclose(dot_product[1], dot_product[2])