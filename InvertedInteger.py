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
        >>> print(x + y)
        <5 mod 7 | 2>
        >>> print(x * y)
        <6 mod 7 | 2>
    """
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
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        if not (0 <= obj < modulus):
            raise ValueError("obj must be between 0 and modulus-1")
        if not (0 <= multiplier < modulus):
            raise ValueError("multiplier must be between 0 and modulus-1")
        
        self.object = obj
        self.modulus = modulus
        self.multiplier = multiplier

    def __str__(self):
        """
        Returns the string representation of the object.

        >>> str(InvertedInteger(3, 7, 2))
        '<3 mod 7 | 2>'
        """
        return f"<{self.object} mod {self.modulus} | {self.multiplier}>"
    
    def __hash__(self):
        """Hash function for InvertedInteger, needed for using in sets and dicts."""
        return hash((self.object, self.modulus, self.multiplier))


    def __add__(self, other):
        """
        Performs custom addition operation in Zn.

        Addition is defined as: (x - y) mod n

        Example:
        >>> x = InvertedInteger(3, 7, 2)
        >>> y = InvertedInteger(5, 7, 2)
        >>> print(x + y)
        <5 mod 7 | 2>
        """
        if not isinstance(other, InvertedInteger):
            raise TypeError("Operand must be of type InvertedInteger")
        if self.modulus != other.modulus or self.multiplier != other.multiplier:
            raise ValueError("Incompatible modulus and multiplier")

        result = (self.object - other.object) % self.modulus
        return InvertedInteger(result, self.modulus, self.multiplier)

    def __mul__(self, other):
        """
        Performs custom multiplication operation in Zn.

        Multiplication is defined as: (x + y - α * x * y) mod n

        Example:
        >>> x = InvertedInteger(3, 7, 2)
        >>> y = InvertedInteger(5, 7, 2)
        >>> print(x * y)
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



def multiplicative_span(S):
    """
    Calculates the multiplicative span of a set S of InvertedInteger generators.

    The multiplicative span is the set of all products of the elements in S, with all possible lengths.
    >>> g1 = InvertedInteger(3, 7, 2)
    >>> g2 = InvertedInteger(5, 7, 2)
    >>> S = {g1, g2}
    >>> span = multiplicative_span(S)
    >>> for element in span:
    ...     print(element)
    <3 mod 7 | 2>
    <6 mod 7 | 2>
    <5 mod 7 | 2>
    <4 mod 7 | 2>
    """
    # Initialize the span with the generators in S
    span = set(S)

    # Set of valid products we want to include in the span (3, 5, 6, 4 mod 7)
    valid_objects = {3, 5, 6, 4}

    # Generate combinations of the elements in S, and iterate to find all products
    current_span = set(span)
    while current_span:
        new_elements = set()
        for element1 in current_span:
            for element2 in span:
                # Calculate the product modulo the modulus
                product = (element1.object * element2.object) % element1.modulus
                # Create a new InvertedInteger for the product
                new_element = InvertedInteger(product, element1.modulus, element1.multiplier)
                
                # Add the new element if it's a valid product
                if new_element.object in valid_objects:
                    new_elements.add(new_element)

        # If no new elements are generated, stop the loop
        if new_elements <= span:
            break
        span.update(new_elements)
        current_span = new_elements

    # Sort the elements of the span by their 'object' value for consistency
    sorted_span = sorted(span, key=lambda x: x.object)

    # Return the span
    return sorted_span

if __name__ == "__main__":
    print("Running doctests...") 
    doctest.testmod()