from IPython import parallel
with drctview.sync_imports():
   import numpy
clients = parallel.Client(profile=’testprofile’)
drctview = clients[:]
drctview.activate()
drctview.block=True
%px dummymatrix = numpy.random.rand(4,4)
%px eigenvalue = numpy.linalg.eigvals(dummymatrix)
drctview['eigenvalue']

%pxconfig --noblock
%autopx
maximum_egnvals = []
for idx in range(50):
    arr = numpy.random.rand(10,10)
    egnvals = numpy.linalg.eigvals(arr)
    maximum_egnvals.append(egnvals[0].real)
%autopx
%pxconfig --block 
%px answer= "The average maximum eigenvalue is: %f"%(sum(maximum_egnvals)/len(maximum_egnvals))
dv['answer']

%%px --block --group-outputs=engine
import numpy as np
arr = np.random.random (4,4)
egnvals = numpy.linalg.eigvals(arr)
print egnvals
egnvals.max()
egnvals.min()

odd_view = clients[1::2]
odd_view.activate("_odd")
%px print "Test Message"
odd_view.block = True
%px print "Test Message"
clients.activate()
%px print "Test Message"
%px_odd print "Test Message"
