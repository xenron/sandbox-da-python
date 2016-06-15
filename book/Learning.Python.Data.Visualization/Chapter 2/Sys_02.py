import sys

pyversion_major = sys.version_info[0];
pyversion_minor = sys.version_info[1];
pyversion_micro = sys.version_info[2];

print("Python version: %s.%s.%s" % (pyversion_major, pyversion_minor, pyversion_micro))
