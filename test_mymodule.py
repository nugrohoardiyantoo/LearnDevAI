import unittest
from mymodule import square, doubler

class TestSquare (unittest.TestCase):
    def test1 (self):
        self.assertEqual(square(2),4)
        self.assertEqual(square(3),9)
        self.assertEqual(square(4),16)

class TestDoubler(unittest.TestCase):
    def test2(self):
        self.assertEqual(doubler(3),6)
        self.assertEqual(doubler(4),8)
        self.assertEqual(doubler(-3),-6)

unittest.main()