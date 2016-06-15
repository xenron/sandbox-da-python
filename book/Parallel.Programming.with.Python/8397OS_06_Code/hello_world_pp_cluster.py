import os, pp

def hello_world(value):
    return "Hello world from hostname [%s] with pid [%d] and number [%d]" % (os.uname()[1], os.getpid(), value) 

node_list = ('192.168.25.20',)
job_server = pp.Server(ppservers=node_list)

result_dict = {}

for i in xrange(10):
    result_dict[i] = job_server.submit(hello_world, args=(i,))

for key, value in result_dict.items():
    print "key [%d] => [%s]" % (key, value())

