import numpy as np
from IPython import parallel
clients = parallel.Client(profile=’testprofile’)
drctview = clients[:]
drctview.push(dict(a=1.03234,b=3453))
drctview.pull(’a’)
drctview.pull(’b’, targets=0)
drctview.pull((’a’,’b’))
drctview.push(dict(c=’speed’))

drctview.scatter(’a’,range(16))
drctview[’a’]
drctview.gather(’a’)

def paralleldot(vw, mat1, mat2):
    vw['mat2'] = mat2
    vw.scatter('mat1', mat1)
    vw.execute('mat3=mat1.dot(mat2)')
    return vw.gather('mat3', block=True)
a = np.matrix('1 2 3; 4 5 6; 7 8 9')
b = np.matrix('4 5 6; 7 8 9; 10 11 12')
paralleldot(dview, a,b)