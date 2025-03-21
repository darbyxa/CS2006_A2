import doctest

class InvertedInteger:
      """
    Represents an element in Zn with a custom inverted integer operation.

    Attributes:
        object (int): The integer value in Zn.
        modulus (int): The modulus n.
        multiplier (int): The multiplier α.

    Example usage:
        >>> x = InvertedInteger(3, 7, 2)
        >>> print(x)
        <3 mod 7 | 2>
        >>> y = InvertedInteger(5, 7, 2)
        >>> x + y
        <5 mod 7 | 2>
        >>> x * y
        <6 mod 7 | 2>
    """
      # obj - integer value in Zn
      # modulus - modulus n is a positive integer
      # multiplier - multiplier alpha in Zn
      def __init__(self, obj, modulus, multiplier):

            """
             Initializes an `InvertedInteger` object.

             >>> i = InvertedInteger(3, 7, 2)
             >>> i.object
             3
            >>> i.modulus
             7
             >>> i.multiplier
            2
             """
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
            """
        Returns the string representation of the object.

        >>> str(InvertedInteger(3, 7, 2))
        '<3 mod 7 | 2>'
        """
            return "<" + str(self.object) + " mod " + str(self.modulus) + " | " + str(self.multiplier) + " >"

       
      def __add__(self, other):
        """
        Performs custom addition operation in Zn.

        Addition is defined as: (x - y) mod n

        Example:
        >>> x = InvertedInteger(3, 7, 2)
        >>> y = InvertedInteger(5, 7, 2)
        >>> x + y
        <5 mod 7 | 2>
        """
        if not isinstance(other, InvertedInteger):
            raise TypeError("Operand must be of type InvertedInteger")
        if self.modulus != other.modulus or self.multiplier != other.multiplier:
            raise ValueError("Incompatible modulus and multiplier")

        result = (self.object - other.object) % self.modulus
        return InvertedInteger(result, self.modulus, self.multiplier)


      # define multiplication = (x + y - a * x * y) mod n
      def __mul__(self, other):
        """
        Performs custom multiplication operation in Zn.

        Multiplication is defined as: (x + y - α * x * y) mod n

        Example:
        >>> x = InvertedInteger(3, 7, 2)
        >>> y = InvertedInteger(5, 7, 2)
        >>> x * y
        <6 mod 7 | 2>
        """
        if not isinstance(other, InvertedInteger):
            raise TypeError("Operand must be of type InvertedInteger")
        if self.modulus != other.modulus or self.multiplier != other.multiplier:
            raise ValueError("Incompatible modulus and multiplier")

        result = (self.object + other.object - self.multiplier * self.object * other.object) % self.modulus
        return InvertedInteger(result, self.modulus, self.multiplier)
      
      def __eq__(self, other):
        """
        Equality check for two InvertedInteger objects.

        Example:
        >>> x = InvertedInteger(3, 7, 2)
        >>> y = InvertedInteger(3, 7, 2)
        >>> x == y
        True
        >>> z = InvertedInteger(5, 7, 2)
        >>> x == z
        False
        """
        if not isinstance(other, InvertedInteger):
            return False
        return (self.object == other.object and
                self.modulus == other.modulus and
                self.multiplier == other.multiplier)

if __name__ == "__main__":
      doctest.testmod()