import unittest

from invertedInteger import InvertedInteger, has_all_idempotents_property, idempotent_pairs, has_commutative_inverted_multiplication, non_commutative_multiplication_pairs, has_commutative_inverted_addition, commutative_addition_pairs, has_associative_inverted_multiplication, associative_multiplication_pairs

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

    def test_idempotency(self):
        self.assertTrue(has_all_idempotents_property(1, 0))
        self.assertTrue(has_all_idempotents_property(2, 5))
        self.assertFalse(has_all_idempotents_property(5, 4))

    def test_idempotentPairs(self):
        self.assertEqual(idempotent_pairs(50), [(1, 0), (2,1)])
        with self.assertRaises(ValueError):
            idempotent_pairs(55)

    # commutative multiplication
    def test_computativity(self):
        self.assertTrue(has_commutative_inverted_multiplication(1, 0))
        self.assertTrue(has_commutative_inverted_multiplication(2, 1))
        # self.assertFalse(has_commutative_inverted_multiplication(3, 1))

    def test_commutativePairs(self):
        self.assertEqual(non_commutative_multiplication_pairs(50), [])
        # self.assertEqual(non_commutative_pairs(2), [(2,0)])
        with self.assertRaises(ValueError):
            non_commutative_multiplication_pairs(78)

    # commutative addition
    def test_has_commutative_inverted_addition(self):
        self.assertTrue(has_commutative_inverted_addition(1, 0))
        self.assertFalse(has_commutative_inverted_addition(5 ,4))

    def test_find_commutative_addition_pairs(self):
        self.assertEqual(non_commutative_multiplication_pairs(50), [])
        with self.assertRaises(ValueError):
            non_commutative_multiplication_pairs(51)

    # associative
    def test_has_associative_inverted_multiplication(self):
        self.assertTrue(has_associative_inverted_multiplication(1, 0))
        self.assertFalse(has_associative_inverted_multiplication(2, 1))
        self.assertFalse(has_associative_inverted_multiplication(3, 2))

    def test_find_associative_pairs(self):
        self.assertEqual(associative_multiplication_pairs(2), [(1, 0)])
        # self.assertEqual(associative_multiplication_pairs(4), [(1, 0), (2, 1), (3, 2), (4, 3)])