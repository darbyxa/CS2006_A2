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

# checks for indempotent x in Zn
def has_all_idempotents_property(n, a):
      for x in range(n):
            if ((x + x - a * x * x) % n) != x:
                  return False
      return True

# finds indempotent pairs
def find_idempotent_pairs():
      pairs = []
      for n in range(1, 51):
            for a in range(n):
                  if has_all_idempotents_property(n, a):
                        pairs.append((n, a))
      return pairs

pairs = find_idempotent_pairs()
for pair in pairs:
      print(pair)