#Program to calculate sum of polynomials 

def sum_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    result = [0] * max_len
    
    for i in range(max_len):
        coeff1 = poly1[i] if i < len(poly1) else 0
        coeff2 = poly2[i] if i < len(poly2) else 0
        result[i] = coeff1 + coeff2
        
    return result
# Example usage:
# poly1 = [1, 2, 3]  # Represents 1 + 2x + 3x^2
# poly2 = [4, 5]     # Represents 4 + 5x
# print(sum_poly(poly1, poly2))  # Output: [5, 7, 3] which represents 5 + 7x + 3x^2
print(sum_poly([1, 2, 3], [4, 5]))  # Example usage