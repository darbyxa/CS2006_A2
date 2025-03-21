from InvertedInteger import InvertedInteger
def multiplicative_span(S):
    """
    Returns the multiplicative span of the set S of InvertedInteger objects.
    """
    span = set()
    
    # Step 1: Add each element of S individually to the span.
    for g in S:
        span.add(g)
    
    # Step 2: Use a list to store combinations of products, starting with individual generators.
    products = list(S)
    
    # Step 3: Start multiplying combinations.
    i = 0
    while i < len(products):
        current = products[i]
        # Try multiplying the current product with each generator in S.
        for g in S:
            new_product = current * g
            if new_product not in span:
                span.add(new_product)
                products.append(new_product)
        i += 1
    
    return span

if __name__ == "__main__":
    # Example usage:
    g1 = InvertedInteger(3, 7, 2)
    g2 = InvertedInteger(5, 7, 2)
    g3 = InvertedInteger(6, 7, 2)
    
    S = {g1, g2, g3}
    
    # Calculate and print the multiplicative span
    span = multiplicative_span(S)
    
    print("Multiplicative Span:")
    for element in span:
        print(element)