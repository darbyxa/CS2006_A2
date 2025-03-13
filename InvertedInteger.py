class InvertedInteger:
      # obj - integer value in Zn
      # modulus - modulus n is a positive integer
      # multiplier - multiplier alpha in Zn
      def __init__(self, obj, modulus, multiplier):
            # checking if arguments are valid
            if modulus <= 0:
                  print("Modulus must be positive.")
            if (modulus <= obj) or (obj <= 0):
                  print("obj must be between 0 and modulus-1")
            if (modulus <= multiplier) or (multiplier <= 0):
                  print("multiplier must be between 0 and modulus-1")
            
            # initialising values
            self.object = obj
            self.modulus = modulus
            self.multiplier = multiplier


      # overwrite "print"
      def __str__(self):
            return "<" + str(self.object) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"

      # defines addition = (x - y) mod n
      def __add__(self, other):
            result = (self.obj - other.obj) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)

      # define multiplication = (x + y - a * x * y) mod n
      def __mul__(self, other):
            result = (self.obj + other.obj - self.multipler * self.obj * other.obj) % self.modulus
            return InvertedInteger(result, self.modulus, self.multiplier)
