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



print("Iterating over InvertedIntegers(3,2):")
for x in InvertedIntegers(3,2):
    print(x)
