#Program to calculate product of two polynomials
# This is a basic implementation and can be optimized further       

def product_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    print(result)

    for i, coeff1 in enumerate(poly1):
        print(f"Processing coefficient {coeff1} at index {i} of poly1")
        for j, coeff2 in enumerate(poly2):
            result[i + j] += coeff1 * coeff2
            print(f"Multiplying {coeff1} (poly1[{i}]) with {coeff2} (poly2[{j}]) and adding to result[{i + j}]")
            print(f"Current result: {result}")

    print("Final result after multiplication:", result)

    return result

print(product_poly([1, 2, 3], [4, 5]))  # Example usage
# Output: [4, 13, 22, 15] which represents 4 + 13x + 22x^2 + 15x^3