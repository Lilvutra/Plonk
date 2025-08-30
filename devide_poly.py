#Program to devide two polynomials
def divide_poly(poly1, poly2):
    """
    Divides two polynomials represented as lists of coefficients.
    
    Args:
        poly1 (list): Coefficients of the dividend polynomial.
        poly2 (list): Coefficients of the divisor polynomial.
    
    Returns:
        list: Coefficients of the quotient polynomial.
    """
    if len(poly2) == 0 or (len(poly2) == 1 and poly2[0] == 0):
        raise ValueError("Division by zero polynomial is not allowed.")
    
    # Initialize quotient and remainder
    quotient = []
    remainder = poly1[:] # Make a copy of the dividend polynomial
    degree_diff = len(poly1) - len(poly2)
    
    while degree_diff >= 0:
        # Calculate the leading coefficient of the quotient
        leading_coeff = remainder[0] / poly2[0]
        quotient.append(leading_coeff)
        
        # Create a term to subtract from the remainder
        term = [leading_coeff * coeff for coeff in poly2] + [0] * degree_diff
        
        # Subtract the term from the remainder
        remainder = [r - t for r, t in zip(remainder, term)]
        
        # Remove leading zeros from the remainder
        while remainder and remainder[0] == 0:
            remainder.pop(0)
        
        degree_diff = len(remainder) - len(poly2)
    
    return quotient     
# Example usage:
# poly1 = [1, 2, 3]  # Represents 1 + 2x + 3x^2
# poly2 = [1, 1]     # Represents 1 + x
# print(divide_poly(poly1, poly2))  # Output: [1.0, 1.0] which represents x + 1
print(divide_poly([1, 2, 3], [1, 1]))  # Example usage
# Output: [1.0, 1.0] which represents x + 1
        