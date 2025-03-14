class InvertedInteger:
      # object - integer value in Zn
      # modulus - modulus n is a positive integer
      # multiplier - multiplier alpha in Zn
      def __init__(self, object, modulus, multiplier):
            # checking if arguments are valid
            if modulus <= 0:
                  print("Modulus must be positive.")
            if (modulus <= object) or (object <= 0):
                  print("object must be between 0 and modulus-1")
            if (modulus <= multiplier) or (multiplier <= 0):
                  print("multiplier must be between 0 and modulus-1")
            
            # initialising values
            self.object = object
            self.modulus = modulus
            self.multiplier = multiplier


      # overwrite "print"
      def __str__(self):
            return "<" + str(self.object) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"

      # defines addition = (x - y) mod n
      def __add__(self, other):
            result = (self.object - other.object) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)

      # defines multiplication = (x + y - a * x * y) mod n
      def __mul__(self, other):
            result = (self.object + other.object - self.multiplier * self.object * other.object) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)
      
      def __eq__(self, other):
            return self.object == other.object and self.modulus == other.modulus and self.multiplier == other.multiplier
