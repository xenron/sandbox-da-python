import os, pp

def hello_world():
    return "Hello world from [%d]" % os.getpid() 

job_server = pp.Server()

task_result1 = job_server.submit(hello_world)
task_result2 = job_server.submit(hello_world)

print task_result1()
print task_result2()

