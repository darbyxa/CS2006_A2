import unittest

from invertedInteger import InvertedInteger

class testing(unittest.TestCase):
    def test_init(self):
        self.assertEqual(str(InvertedInteger(3, 7, 2)), "<3 mod 7 | 2 >")
    
    def test_add(self):
        x = InvertedInteger(3, 7, 2)
        y = InvertedInteger(5, 7, 2)
        self.assertEqual(x + y, InvertedInteger(5, 7, 2))

    def test_mul(self):
        x = InvertedInteger(3, 7, 2)
        y = InvertedInteger(5, 7, 2)
        self.assertEqual(x * y, InvertedInteger(6, 7, 2))

    def test_mulSame(self):
        x = InvertedInteger(3, 7, 2)
        self.assertEqual(x * x, InvertedInteger(2, 7, 2))