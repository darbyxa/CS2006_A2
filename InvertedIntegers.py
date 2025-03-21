import time

class InvertedInteger:
    def __init__(self, obj, modulus, multiplier):
        # Ensures the modulus is positive and the object falls within the proper range
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        if not (0 <= obj < modulus):
            raise ValueError("Object must be between 0 and modulus-1")
        # The multiplier must be between 0 and modulus - 1, except when n = 1 where it can be 0
        if not (0 <= multiplier < modulus):  
            raise ValueError("Multiplier must be between 0 and modulus-1")

        self.object = obj
        self.modulus = modulus
        self.multiplier = multiplier

    def __str__(self):
        return f"<{self.object} mod {self.modulus} | {self.multiplier}>"

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
        # Initializes the modulus and multiplier with checks
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        if not (0 <= multiplier < modulus):
            raise ValueError("Multiplier must be between 0 and modulus-1")

        self.modulus = modulus
        self.multiplier = multiplier

    def __iter__(self):
        """Returns an iterator that iterates over all elements in Zn."""
        return (InvertedInteger(i, self.modulus, self.multiplier) for i in range(self.modulus))


def inverted_roots_of_unity(n, alpha):
    """Finds all x in Zn such that x ⊗ x = 1 (i.e., x^2 ≡ 1 mod n)."""
    if n == 1:
        # Special case for Z1, where 0 and 1 are treated equivalently
        if alpha != 0:  # Prevents invalid alpha values outside the allowed range
            return []
        return [InvertedInteger(0, 1, 0)]  # Zn = {0}, and 0 ≡ 1 mod 1

    # Create the identity element 1 in Zn
    unity = InvertedInteger(1, n, alpha)  
    roots = []

    for x in range(n):
        xi = InvertedInteger(x, n, alpha)
        if xi * xi == unity:
            roots.append(xi)

    return roots


def count_inverted_roots_of_unity():
    """Finds the maximum count of inverted roots of unity for 1 ≤ n ≤ 25, 0 ≤ α < n."""
    max_roots = 0
    best_cases = []

    for n in range(1, 26):
        for alpha in range(n):
            roots = inverted_roots_of_unity(n, alpha)
            num_roots = len(roots)

            if num_roots > max_roots:
                max_roots = num_roots
                best_cases = [(n, alpha, roots)]
            elif num_roots == max_roots:
                best_cases.append((n, alpha, roots))

    return max_roots, best_cases


# Running the function to find the maximum case
max_roots, best_cases = count_inverted_roots_of_unity()

# Displaying the best cases
print("Max Number of Inverted Roots of Unity:", max_roots)
for n, alpha, roots in best_cases:
    print(f"n = {n}, alpha = {alpha}, Roots:", [str(r) for r in roots])


# Performance Testing
def compare_performance():
    test_n = 5 
    test_alpha = 2

    print("\nPerformance comparison using direct loops vs iterators:\n")

    start_time = time.time()
    results_loops = [(x, (x + x - test_alpha * x * x) % test_n == x) for x in range(test_n)]
    end_time = time.time()
    print(f"Direct Loop Execution Time: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    results_iterators = [(x, (x.object + x.object - test_alpha * x.object * x.object) % test_n == x.object)
                         for x in InvertedIntegers(test_n, test_alpha)]
    end_time = time.time()
    print(f"Iterator Execution Time: {end_time - start_time:.6f} seconds")


# Testing the iterator with an example
print("Iterating over InvertedIntegers(3, 2):")
for x in InvertedIntegers(3, 2):
    print(x)

# Running performance comparison
compare_performance()
