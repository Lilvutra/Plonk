# Lagrange interpolation 
from product_poly import product_poly
from sum_poly import sum_poly

def interpolate():
    points = [(0, 1), (1, 2), (2, 3)]  # Example points
    n = len(points)
    coeffs = [0] * n

    for i in range(n):
        xi, yi = points[i]
        term = [1]  # Start with the constant polynomial 1

        for j in range(n):
            if i != j:
                xj, _ = points[j]
                term = product_poly(term, [-xj, 1])  # Multiply by (x - xj)

        term = [c * yi for c in term]  # Scale by yi
        coeffs = sum_poly(coeffs, term)  # Add to the result

    return coeffs           
# Example usage:
# print(interpolate())  # Output: Coefficients of the interpolating polynomial
print(f"after interpolating: {interpolate()}")  # Example usage
# Output: Coefficients of the interpolating polynomial
# This will print the coefficients of the polynomial that passes through the given points.      