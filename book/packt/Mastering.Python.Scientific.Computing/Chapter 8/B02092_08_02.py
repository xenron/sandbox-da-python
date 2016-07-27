from IPython import parallel
clients = parallel.Client(profile=’testprofile’)
lbview = clients.load_balanced_view()
lbview.block = True
serial_computation = map(lambda i:i**5, range(26))
parallel_computation = lbview.map(lambda i: i**5, range(26))
@lbview.parallel()
def func_turned_as_parallel(x):
     return x**8
func_turned_as_parallel.map(range(26))