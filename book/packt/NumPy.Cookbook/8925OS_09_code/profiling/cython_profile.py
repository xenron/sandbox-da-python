import pstats
import cProfile
import pyximport
pyximport.install()

import approxe
cProfile.runctx("approxe.approx_e()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()

