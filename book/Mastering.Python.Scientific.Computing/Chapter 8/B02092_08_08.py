from IPython.parallel import *
clients = ipp.Client(profile='testprofile')
lbview = clients.load_balanced_view()

task_fail = lbview.apply_async(lambda : 1/0)
task_success = lbview.apply_async(lambda : 'success')
clients.wait()
print("Fail task executed on %i" % task_fail.engine_id)
print("Success task executed on %i" % task_success.engine_id)

with lbview.temp_flags(after=task_success):
    print(lbview.apply_sync(lambda : 'Perfect'))

with lbview.temp_flags(follow=pl.Dependency([task_fail, task_success], failure=True)):
    lbview.apply_sync(lambda : "impossible")

with lbview.temp_flags(after=Dependency([task_fail, task_success], failure=True, success=False)):
    lbview.apply_sync(lambda : "impossible")

def execute_print_engine(**flags):
    for idx in range(4):
        with lbview.temp_flags(**flags):
            task = lbview.apply_async(lambda : 'Perfect')
            task.get()
            print("Task Executed on %i" % task.engine_id)

execute_print_engine(follow=Dependency([task_fail, task_success], all=False))
execute_print_engine(after=Dependency([task_fail, task_success], all=False))
execute_print_engine(follow=Dependency([task_fail, task_success], all=False, failure=True, success=False))
execute_print_engine(follow=Dependency([task_fail, task_success], all=False, failure=True))