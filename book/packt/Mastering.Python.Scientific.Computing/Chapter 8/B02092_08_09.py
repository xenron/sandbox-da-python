import multiprocessing as mpcs
import random
import string

output_queue = mpcs.Queue()

def strings_random(len, output_queue):
	generated_string = ''.join(random.choice(string.ascii_lowercase	+ string.ascii_uppercase + string.digits)
		for i in range(length))
	output_queue.put(generated_string)

procs = [mpcs.Process(target=strings_random, args=(8, output_queue)) for i in range(7)]

for proc in procs:
	proc.start()

for proc in procs:
	proc.join()

results = [output_queue.get() for pro in procs]
print(results)