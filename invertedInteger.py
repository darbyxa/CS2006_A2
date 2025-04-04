class InvertedInteger:
      # value - integer value in Zn
      # modulus - modulus n is a positive integer
      # multiplier - multiplier alpha in Zn
      def __init__(self, value, modulus, multiplier):
            # checks if arguments are valid
            if modulus <= 0:
                  raise ValueError("Modulus must be positive.")
            if not (0 <= value < modulus):
                  raise ValueError("Value must be between 0 and modulus-1")
            if not (0 <= multiplier < modulus):
                  raise ValueError("multiplier must be between 0 and modulus-1")
            
            # initialises values
            self.value = value
            self.modulus = modulus
            self.multiplier = multiplier


      # prints current instance of invertedInteger
      def __str__(self):
            return "<" + str(self.value) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"

      # defines addition = (x - y) mod n
      def __add__(self, other):
            if not isinstance(other, InvertedInteger):
                  raise TypeError("y must be of type InvertedInteger")
            if (self.modulus != other.modulus) or (self.multiplier != other.multiplier):
                  raise ValueError("Incompatible as modulus and multiplier must match")
            
            result = (self.value - other.value) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)

      # defines multiplication = (x + y - a * x * y) mod n
      def __mul__(self, other):
            if not isinstance(other, InvertedInteger):
                  raise TypeError("y must be of type InvertedInteger")
            if (self.modulus != other.modulus) or (self.multiplier != other.multiplier):
                  raise ValueError("Incompatible as modulus and multiplier must match")

            result = (self.value + other.value - self.multiplier * self.value * other.value) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)
      
      # checks if value values are equal
      def __eq__(self, other):
            if not isinstance(other, InvertedInteger):
                  raise TypeError("Values must be of type InvertedInteger")

            return self.value == other.value and self.modulus == other.modulus and self.multiplier == other.multiplier

# checks for idempotency x in Zn
def has_all_idempotents_property(n, alpha):
      for x in range(n):
            if ((x + x - alpha * x * x) % n) != x:
                  return False
      return True

# finds idempotent pairs
def idempotent_pairs(max):
      if 1 <= max <= 50:
            pairs = []
            for n in range(1, max+1):
                  for alpha in range(n):
                        if has_all_idempotents_property(n, alpha):
                              pairs.append((n, alpha))
            return pairs
      raise ValueError("n must be between 1 and 50 inclusive")

# checks for commutativity in multiplication
def has_commutative_inverted_multiplication(n, alpha):
      for x in range(n):
            for y in range(x, n):   # starts from x to avoid redundant calculations
                  if ((x + y - alpha * x * y) % n) != ((y + x - alpha * y * x) % n):
                        return False
      return True

# checks for non commutative pairs
def non_commutative_multiplication_pairs(max):
      if 1 <= max <= 50:
            pairs = []
            for n in range(1, max+1):
                  for alpha in range(n):
                        if not has_commutative_inverted_multiplication(n, alpha):
                              pairs.append((n, alpha))
            return pairs
      raise ValueError("n must be between 1 and 50 inclusive")

# checks for commutativity in addition
def has_commutative_inverted_addition(n, alpha):
      for x in range(n):
            for y in range(x, n):  # begins at x to skip redundant calculations
                  if ((x - y) % n) != ((y - x) % n):
                        return False
      return True

# finds commutative pairs in addition
def commutative_addition_pairs(max):
      if 1 <= max <= 50:
            pairs = []
            for n in range(1, max+1):
                  for alpha in range(n):
                        if not has_commutative_inverted_addition(n, alpha):
                              pairs.append((n, alpha))
            return pairs
      raise ValueError("n must be between 1 and 50 inclusive")

# checks for associativity in multiplication
def has_associative_inverted_multiplication(n, alpha):
      for x in range(n):
            for y in range(n):
                  for z in range(n):
                        # calculates left part of the equation
                        xy = (x + y - alpha * x * y) % n
                        l = (xy + z - alpha * xy * z) % n

                        # calculates right part of the equation
                        yz = (y + z - alpha * y * z) % n
                        r = (x + yz - alpha * x * yz) % n

                        # checks if they equal
                        if l != r:
                              return False
      return True

# check for associative multiplication pairs
def associative_multiplication_pairs(max):
      if 1 <= max <= 20:
            pairs = []
            for n in range(1, max+1):
                  for alpha in range(n):
                        if has_associative_inverted_multiplication(n, alpha):
                              pairs.append((n, alpha))
            return pairs
      raise ValueError("n must be between 1 and 20 inclusive")

# checks for associativity in addition
def has_associative_inverted_addition(n, alpha):
      for x in range(n):
            for y in range(n):
                  for z in range(n):
                        # calculates left part of the equation
                        xy = (x - y) % n
                        l = (xy - z) % n

                        # calculates right part of the equation
                        yz = (y - z) % n
                        r = (x - yz) % n

                        # checks if they equal
                        if l != r:
                              return False
      return True

# check for associative addition pairs
def associative_addition_pairs(max):
      if 1 <= max <= 20:
            pairs = []
            for n in range(1, max+1):
                  for alpha in range(n):
                        if has_associative_inverted_addition(n, alpha):
                              pairs.append((n, alpha))
            return pairs
      raise ValueError("n must be between 1 and 20 inclusive")

# checks for right distributivity
def has_inverted_right_distributivity(n, alpha):
      for x in range(n):
            for y in range(n):
                  for z in range(n):
                        # calculates left part of the equation
                        xy = (x - y) % n
                        l = (xy + z - alpha * xy * z) % n

                        # calculates right part of the equation
                        xz = (x + z - alpha * x * z) % n
                        yz = (y + z - alpha * y * z) % n
                        r = (xz - yz) % n

                        # checks if they equal
                        if l != r:
                              return False
      return True

# check for distributive pairs
def distributivity_pairs(max):
      if 1 <= max <= 20:
            pairs = []
            for n in range(1, max+1):
                  for alpha in range(n):
                        if has_inverted_right_distributivity(n, alpha):
                              pairs.append((n, alpha))
            return pairs
      raise ValueError("n must be between 1 and 20 inclusive")