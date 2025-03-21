import unittest

from invertedInteger import (
    InvertedInteger, 
    has_all_idempotents_property, 
    idempotent_pairs, 
    has_commutative_inverted_multiplication, 
    non_commutative_multiplication_pairs, 
    has_commutative_inverted_addition, 
    commutative_addition_pairs, 
    has_associative_inverted_multiplication, 
    associative_multiplication_pairs, 
    has_associative_inverted_addition, 
    associative_addition_pairs, 
    has_inverted_right_distributivity, 
    distributivity_pairs
)

class testing(unittest.TestCase):
    def test_init(self):
        self.assertEqual(str(InvertedInteger(3, 7, 2)), "<3 mod 7 | 2 >")
    
    # tests the definitions
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

    # testing definitions by generating a multiplication table
    def test_mulTable(self):
        n = 5
        alpha = 2
        invertedInts = [InvertedInteger(x, n, alpha) for x in range(n)]
        
        # generated table
        genTable = [[(x * y).value for y in invertedInts] for x in invertedInts]
        # expected table
        expTable = [
            [0, 1, 2, 3, 4],
            [1, 0, 4, 3, 2],
            [2, 4, 1, 3, 0],
            [3, 3, 3, 3, 3],
            [4, 2, 0, 3, 1],
        ]

        self.assertEqual(genTable, expTable)

    # testing definitions by finding all inverted roots of unity
    def test_rootsOfUnity(self):
        n = 5
        alpha = 2
        roots = []
        for x in range(n):
            if (InvertedInteger(x, n, alpha) * InvertedInteger(x, n, alpha)) == InvertedInteger(1, n, alpha):
                roots.append(x)

        self.assertEqual(roots, [2, 4])

    # idempotency tests
    def test_idempotency(self):
        self.assertTrue(has_all_idempotents_property(1, 0))
        self.assertTrue(has_all_idempotents_property(2, 1))
        self.assertTrue(has_all_idempotents_property(2, 5))
        self.assertFalse(has_all_idempotents_property(5, 4))
        self.assertFalse(has_all_idempotents_property(5, 2))

    def test_idempotentPairs(self):
        self.assertEqual(idempotent_pairs(50), [(1, 0), (2,1)])
        with self.assertRaises(ValueError):
            idempotent_pairs(51)
        with self.assertRaises(ValueError):
            idempotent_pairs(-1)

    # commutative multiplication
    def test_computativityMultiplication(self):
        self.assertTrue(has_commutative_inverted_multiplication(1, 0))
        self.assertTrue(has_commutative_inverted_multiplication(2, 1))
        self.assertTrue(has_commutative_inverted_multiplication(5, 2))

    def test_commutativeMultiplicationPairs(self):
        self.assertEqual(non_commutative_multiplication_pairs(50), [])
        self.assertEqual(non_commutative_multiplication_pairs(5), [])
        with self.assertRaises(ValueError):
            non_commutative_multiplication_pairs(51)

    # commutative addition
    def test_commutativeAddition(self):
        self.assertTrue(has_commutative_inverted_addition(1, 0))
        self.assertTrue(has_commutative_inverted_addition(2, 1))
        self.assertFalse(has_commutative_inverted_addition(5, 2))
        self.assertFalse(has_commutative_inverted_addition(5 ,4))

    def test_commutativeAdditionPairs(self):
        self.assertEqual(commutative_addition_pairs(1), [])
        self.assertEqual(commutative_addition_pairs(3), [(3, 0), (3, 1), (3, 2)])
        with self.assertRaises(ValueError):
            commutative_addition_pairs(51)

    # associative multiplication
    def test_associativeMultiplication(self):
        self.assertTrue(has_associative_inverted_multiplication(1, 0))
        self.assertTrue(has_associative_inverted_multiplication(2, 1))
        self.assertTrue(has_associative_inverted_multiplication(5, 2))

    def test_associativeMultiplicationPairs(self):
        self.assertEqual(associative_multiplication_pairs(2), [(1, 0), (2, 0), (2, 1)])
        self.assertEqual(associative_multiplication_pairs(1), [(1, 0)])
        with self.assertRaises(ValueError):
            associative_multiplication_pairs(21)
        with self.assertRaises(ValueError):
            associative_multiplication_pairs(0)

    # associative addition
    def test_associativeMultiplication(self):
        self.assertTrue(has_associative_inverted_addition(1, 0))
        self.assertTrue(has_associative_inverted_addition(2, 1))
        self.assertFalse(has_associative_inverted_addition(5, 2))

    def test_associativeAdditionPairs(self):
        self.assertEqual(associative_addition_pairs(3), [(1, 0), (2, 0), (2, 1)])
        self.assertEqual(associative_addition_pairs(2), associative_addition_pairs(3))
        with self.assertRaises(ValueError):
            associative_addition_pairs(21)
        
    # right distributivity
    def test_distributivity(self):
        self.assertTrue(has_inverted_right_distributivity(1, 0))
        self.assertFalse(has_inverted_right_distributivity(2, 1))
        self.assertFalse(has_inverted_right_distributivity(5, 2))

    def test_distributivityPairs(self):
        self.assertEqual(distributivity_pairs(5), [(1, 0)])
        with self.assertRaises(ValueError):
            distributivity_pairs(21)

if __name__ == "__main__": 
       unittest.main()  
