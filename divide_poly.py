def divide_poly(f, g):
    f = f[:]  # copy
    deg_f = len(f) - 1
    deg_g = len(g) - 1
    if deg_f < deg_g:
        return [0], f

    quotient = [0] * (deg_f - deg_g + 1)
   
    while len(f) >= len(g):
        lead_coeff = f[-1] / g[-1]  # Assumes field (e.g., float or mod inverse)
        print(f"Lead coefficient: {lead_coeff}")
        deg_diff = len(f) - len(g)
        print(f"Degree difference: {deg_diff}")
        quotient[deg_diff] = lead_coeff
        print(f"Quotient so far: {quotient}")
        # lead_coeff has the coefficient of x^deg_diff in the quotient

        # Subtract lead_coeff * g shifted
        for i in range(len(g)):
            print(f"Subtracting {lead_coeff} * {g[i]} from f[{deg_diff + i}]")
            f[deg_diff + i] -= lead_coeff * g[i]  # deg_diff: how far you must shift the divisor to line up with the dividend’s leading term

        # Remove leading zero if needed
        while f and abs(f[-1]) < 1e-9:  
            f.pop()

    return quotient, f  # quotient, remainder
  
# Example usage:
# poly1 = [1, 2, 3]  # Represents 1 + 2x + 3x^2
# poly2 = [1, 1]     # Represents 1 + x
# print(devide_poly(poly1, poly2))  # Output: [1.0, 1.0] which represents x + 1
print(divide_poly([1, 2, 3], [1, 1]))  # Example usage
# Output: [1.0, 1.0] which represents x + 1
        