class InvertedInteger:
      # object - integer value in Zn
      # modulus - modulus n is a positive integer
      # multiplier - multiplier alpha in Zn
      def __init__(self, object, modulus, multiplier):
            # checking if arguments are valid
            if modulus <= 0:
                  raise ValueError("Modulus must be positive.")
            if (modulus <= object) or (object <= 0):
                  raise ValueError("object must be between 0 and modulus-1")
            if (modulus <= multiplier) or (multiplier <= 0):
                  raise ValueError("multiplier must be between 0 and modulus-1")
            
            # initialising values
            self.object = object
            self.modulus = modulus
            self.multiplier = multiplier


      # overwrite "print"
      def __str__(self):
            return "<" + str(self.object) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"

      # defines addition = (x - y) mod n
      def __add__(self, other):
            if not isinstance(other, InvertedInteger):
                  raise TypeError("y must be of type InvertedInteger")
            if (self.modulus != other.modulus) or (self.multiplier != other.multiplier):
                  raise ValueError("Incompatible as modulus and multiplier must match")
            
            result = (self.object - other.object) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)

      # defines multiplication = (x + y - a * x * y) mod n
      def __mul__(self, other):
            if not isinstance(other, InvertedInteger):
                  raise TypeError("y must be of type InvertedInteger")
            if (self.modulus != other.modulus) or (self.multiplier != other.multiplier):
                  raise ValueError("Incompatible as modulus and multiplier must match")

            result = (self.object + other.object - self.multiplier * self.object * other.object) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)
      
      def __eq__(self, other):
            if not isinstance(other, InvertedInteger):
                  raise TypeError("Values must be of type InvertedInteger")

            return self.object == other.object and self.modulus == other.modulus and self.multiplier == other.multiplier

# checks for idempotency x in Zn
def has_all_idempotents_property(n, a):
      for x in range(n):
            if ((x + x - a * x * x) % n) != x:
                  return False
      return True

# finds idempotent pairs
def idempotent_pairs(max):
      if 1 <= max <= 50:
            pairs = []
            for n in range(1, max+1):
                  for a in range(n):
                        if has_all_idempotents_property(n, a):
                              pairs.append((n, a))
            return pairs
      raise ValueError("n must be between 1 and 50 inclusive")

# pairs = idempotent_pairs()
# for pair in pairs:
#       print(pair)


# checks for commutativity in Zn
def has_commutative_inverted_multiplication(n, a):
      for x in range(n):
            for y in range(x, n):   # start from x to avoid redundant calculations
                  if ((x + y - a * x * y) % n) != ((y + x - a * y * x) % n):
                        return False
      return True

# checks for commutative pairs
def non_commutative_pairs(max):
      if 1 <= max <= 50:
            pairs = []
            for n in range(1, max+1):
                  for a in range(n):
                        if not has_commutative_inverted_multiplication(n, a):
                              pairs.append((n,a))
            return pairs
      raise ValueError("n must be between 1 and 50 inclusive")

# pairs = non_commutative_pairs(2)
# for pair in pairs:
#       print("pair")
#       print(pair)