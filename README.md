## Git repository link
https://github.com/darbyxa/CS2006_A2.git

## Introduction
This program provides a python module for working with inverted integers. The InvertedInteger class defines specialised multiplication and additions operations:

- x + y = (x - y) % n
- x * y = (x + y - alpha * x * y) % n

This module is designed to help explore the properties (e.g commutativity, associativity) of these operations interactively.

## Dependencies
- Python3 is required
- No additional dependencies needed

## Loading program
Start the python interpreter in the terminal:
    python3

Load the module:
    from invertedInteger import InvertedInteger

## Interactive testing
Example1 - basic test:
from invertedInteger import InvertedInteger
x = InvertedInteger(3, 7, 2)
y = InvertedInteger(5, 7, 2)
print(x)
print(x * y)
print(x + y)

Output:
<3 mod 7 | 2>
<6 mod 7 | 2>
<5 mod 7 | 2>

Example2 - checking idempotency:
from invertedInteger import has_all_idempotents_property, idempotent_pairs
print(has_all_idempotents_property(5, 4))
print(find_all_idempotent_pairs(5))

Output:
False
[(1, 0), (2, 1)]

Example3 - checking associativity:
from invertedInteger import has_associative_inverted_multiplication
print([(n, alpha) for n in range(1, 6) for alpha in range(n) if has_associative_inverted_multiplication(n, alpha)])

Example4 - creating a multiplication table:
from invertedInteger import InvertedInteger
n, alpha = 5, 2
invertedInts = [InvertedInteger(x, n, alpha) for x in range(n)]
table = [[(x * y).value for y in invertedInts] for x in invertedInts]
print(table)

Output:
[[0, 1, 2, 3, 4], [1, 0, 4, 3, 2], [2, 4, 1, 3, 0], [3, 3, 3, 3, 3], [4, 2, 0, 3, 1]]

Example5 - roots of unity:
roots = [(n, alpha, x) for n in range(1, 6) for alpha in range(n) for x in range(n-1) if (InvertedInteger(x, n, alpha) * InvertedInteger(x, n, alpha)) == InvertedInteger(1, n, alpha)]
print(roots)

Output:
[(3, 1, 1), (4, 1, 1), (5, 0, 3), (5, 1, 1), (5, 2, 2)]

## Running automated tests
Execute the following command in the terminal to run all unit tests:

    python -m unittest -v testing.py

- v flag gives a more verbose result

## Running docTests
Execute the following command in the terminal to run all unit tests:

    python -m doctest InvertedInteger.py -v
    
- v flag gives a more verbose result

## Ending note
Hope you find this module helpful!