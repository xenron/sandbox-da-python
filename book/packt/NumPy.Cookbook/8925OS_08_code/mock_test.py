from mock import MagicMock
import numpy
import unittest

class NuclearReactor():
   def __init__(self, n):
      self.n = n

   def do_work(self, msg):
      print "Working"

      return self.factorial(self.n, msg)

   def factorial(self, n, msg):
      print msg 

      if n == 0:
         return 1

      if n < 0:
         raise ValueError, "Core meltdown"

      return numpy.arange(1, n+1).cumprod()

class NuclearReactorTest(unittest.TestCase):
   def test_called(self):
      reactor = NuclearReactor(3)
      reactor.factorial = MagicMock(return_value=6)
      result = reactor.do_work("mocked")
      self.assertEqual(6, result)
      reactor.factorial.assert_called_with(3, "mocked")

   def test_unmocked(self):
      reactor = NuclearReactor(3)
      reactor.factorial(3, "unmocked")
      numpy.testing.assert_raises(ValueError)

if __name__ == '__main__':
    unittest.main()
