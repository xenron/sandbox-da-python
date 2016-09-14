
import numpy as np
from __future__ import division

def random_wasd(wasd):
    rd = np.random.randint(1, 20)
    min_key = wasd.keys()[np.argmin(wasd.values())]
    return {min_key:rd}

def merge_sum(x, y):
    return { k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y) }

wasd = {"w":1,"a":2,"s":3,"d":4}

delta = random_wasd(wasd)
for i in range(10):
    print("------------------------")
    delta = random_wasd(wasd)
    print(delta)
    wasd = merge_sum(wasd, delta)
    print(wasd)
    print("sum: %s, avg: %s, ptp: %s" % (np.sum(wasd.values()), np.average(wasd.values()), np.ptp(wasd.values())))

