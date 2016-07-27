from IPython.parallel import Client
c = Client(profile='mpi')
view = c[:]
view.activate() # enable magics
view.run('psum.py')
view.scatter('a',np.arange(16,dtype='float'))
view['a']
%px totalsum = psum(a)
view['totalsum']