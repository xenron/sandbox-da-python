import multiprocessing as mpcs
import random
import string

output_queue = mpcs.Queue()

def strings_random(len, position, output_queue):
	generated_string = ''.join(random.choice(string.ascii_lowercase	+ string.ascii_uppercase + string.digits)
		for i in range(length))
	output_queue.put((position, rand_str))

procs = [mp.Process(target=rand_string, args=(5, pos, output)) for pos in range(4)]

for proc in procs:
	proc.start()

for proc in procs:
	proc.join()

results = [output_queue.get() for pro in procs]
results.sort()
results = [rslt[1] for rslt in results]
print(results)