import unittest

from invertedInteger import InvertedInteger, has_all_idempotents_property, find_idempotent_pairs

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

    def test_incompatible(self):
        x = InvertedInteger(3, 7, 2)
        y = InvertedInteger(5, 8, 2)

        with self.assertRaises(ValueError):
            x + y
        with self.assertRaises(ValueError):
            x * y

    def test_idempotent(self):
        self.assertTrue(has_all_idempotents_property(1, 0))
        self.assertTrue(has_all_idempotents_property(2, 5))
        self.assertFalse(has_all_idempotents_property(5, 4))

    def test_idempotentPairs(self):
        pairs = [(1, 0), (2,1)]
        self.assertEqual(find_idempotent_pairs(), pairs)
