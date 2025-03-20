import time

class InvertedInteger:
    def __init__(self, obj, modulus, multiplier):
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        if not (0 <= obj < modulus):
            raise ValueError("Object must be between 0 and modulus-1")
        if not (0 < multiplier < modulus):
            raise ValueError("Multiplier must be between 0 and modulus-1")

        self.object = obj
        self.modulus = modulus
        self.multiplier = multiplier

    def __str__(self):
        return f"<{self.object} mod {self.modulus} | {self.multiplier} >"

    def __add__(self, other):
        if not isinstance(other, InvertedInteger):
            raise TypeError("Operand must be of type InvertedInteger")
        if self.modulus != other.modulus or self.multiplier != other.multiplier:
            raise ValueError("Incompatible modulus and multiplier")

        result = (self.object - other.object) % self.modulus
        return InvertedInteger(result, self.modulus, self.multiplier)

    def __mul__(self, other):
        if not isinstance(other, InvertedInteger):
            raise TypeError("Operand must be of type InvertedInteger")
        if self.modulus != other.modulus or self.multiplier != other.multiplier:
            raise ValueError("Incompatible modulus and multiplier")

        result = (self.object + other.object - self.multiplier * self.object * other.object) % self.modulus
        return InvertedInteger(result, self.modulus, self.multiplier)

    def __eq__(self, other):
        if not isinstance(other, InvertedInteger):
            return False
        return (self.object == other.object and 
                self.modulus == other.modulus and 
                self.multiplier == other.multiplier)


class InvertedIntegers:
    def __init__(self, modulus, multiplier):
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        if not (0 < multiplier < modulus):
            raise ValueError("Multiplier must be between 0 and modulus-1")

        self.modulus = modulus
        self.multiplier = multiplier

    def __iter__(self):
        """Return an iterator over all elements in Zn."""
        return (InvertedInteger(i, self.modulus, self.multiplier) for i in range(self.modulus))


# Property (1): Idempotent Property Check Using Iterators
def has_all_idempotents_property(n, alpha):
    return all((x + x - alpha * x * x) % n == x for x in range(n))

# Property (2): Commutativity in Multiplication
def has_commutative_inverted_multiplication(n, alpha):
    return all(
        (x + y - alpha * x * y) % n == (y + x - alpha * y * x) % n
        for x in range(n) for y in range(x, n)
    )

# Property (3): Commutativity in Addition
def has_commutative_inverted_addition(n, alpha):
    return all(
        (x - y) % n == (y - x) % n
        for x in range(n) for y in range(x, n)
    )

# Property (4): Associativity in Multiplication
def has_associative_inverted_multiplication(n, alpha):
    return all(
        ((x + y - alpha * x * y) + z - alpha * (x + y - alpha * x * y) * z) % n ==
        (x + (y + z - alpha * y * z) - alpha * x * (y + z - alpha * y * z)) % n
        for x in range(n) for y in range(n) for z in range(n)
    )

# Property (5): Associativity in Addition
def has_associative_inverted_addition(n, alpha):
    return all(
        ((x - y) - z) % n == (x - (y - z)) % n
        for x in range(n) for y in range(n) for z in range(n)
    )

# Property (6): Right Distributivity
def has_inverted_right_distributivity(n, alpha):
    return all(
        ((x - y) + z - alpha * (x - y) * z) % n ==
        ((x + z - alpha * x * z) - (y + z - alpha * y * z)) % n
        for x in range(n) for y in range(n) for z in range(n)
    )

# Performance Testing
def compare_performance():
    test_n = 5  # Small test modulus for comparison
    test_alpha = 2

    print("\nPerformance comparison using direct loops vs iterators:\n")

    start_time = time.time()
    results_loops = [(x, has_all_idempotents_property(test_n, test_alpha)) for x in range(test_n)]
    end_time = time.time()
    print("Direct Loop Execution Time:", round(end_time - start_time, 6), "seconds")

    start_time = time.time()
    results_iterators = [(x, has_all_idempotents_property(test_n, test_alpha)) for x in InvertedIntegers(test_n, test_alpha)]
    end_time = time.time()
    print("Iterator Execution Time:", round(end_time - start_time, 6), "seconds")


# Testing the iterator with example 
print("Iterating over InvertedIntegers(3,2):")
for x in InvertedIntegers(3,2):
    print(x)

# Running performance comparison
compare_performance()
