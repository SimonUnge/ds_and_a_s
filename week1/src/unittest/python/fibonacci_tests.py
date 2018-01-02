import unittest
from fibonacci import calc_fib

class FibonacciTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(0, calc_fib(0))
    def test_1(self):
        self.assertEqual(1, calc_fib(1))
    def test_2(self):
        self.assertEqual(1, calc_fib(2))
    def test_3(self):
        self.assertEqual(2, calc_fib(3))
    def test_39(self):
        self.assertEqual(63245986, calc_fib(39))
